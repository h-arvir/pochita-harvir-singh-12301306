"""
Pochita Backend - FastAPI Application
AI agents for collaborative code generation and testing
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from typing import List, Dict, Optional

from agents.architect import ArchitectAgent
from agents.coder import CoderAgent
from agents.tester import TesterAgent
from agents.conversation_manager import ConversationManager
from agents.executor import CodeExecutor
from agents.result_parser import ResultParser

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Pochita API",
    description="AI agents for code generation and testing",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents
architect_agent = ArchitectAgent()
coder_agent = CoderAgent()
tester_agent = TesterAgent()
conversation_manager = ConversationManager()
code_executor = CodeExecutor()

current_code = ""
current_tests = ""
current_prompt = ""


# Request/Response Models
class GenerateRequest(BaseModel):
    prompt: str
    description: Optional[str] = ""


class ExecuteRequest(BaseModel):
    code: str
    tests: str


class Message(BaseModel):
    role: str
    content: str
    agent_type: Optional[str] = None
    timestamp: Optional[str] = None


class GenerateResponse(BaseModel):
    status: str
    code: str
    tests: str
    conversation: List[Message]


# Root Endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "status": "ok",
        "message": "Pochita API"
    }


# Health Check Endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running"""
    return {
        "status": "healthy",
        "message": "Pochita API is running",
        "gemini_configured": bool(os.getenv("GEMINI_API_KEY"))
    }


# Generate Endpoint
@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """Generate code and tests using AI agents"""
    global current_code, current_tests, current_prompt
    try:
        conversation_manager.clear()
        current_prompt = request.prompt
        
        conversation_manager.add_message(
            role="user",
            content=request.prompt,
            agent_type="user"
        )
        
        conversation_manager.add_message(
            role="system",
            content="Architect agent is analyzing requirements...",
            agent_type="system"
        )
        
        architect_analysis = architect_agent.generate(request.prompt)
        
        conversation_manager.add_message(
            role="architect",
            content=architect_analysis,
            agent_type="architect"
        )
        
        coder_prompt = f"{request.prompt}\n\nAdditional context: {request.description}" if request.description else request.prompt
        
        conversation_manager.add_message(
            role="system",
            content="Coder agent is generating code...",
            agent_type="system"
        )
        
        generated_code = coder_agent.generate(coder_prompt)
        current_code = generated_code
        
        conversation_manager.add_message(
            role="coder",
            content=generated_code,
            agent_type="coder"
        )
        
        conversation_manager.add_message(
            role="system",
            content="Tester agent is generating tests...",
            agent_type="system"
        )
        
        test_requirements = f"Test the following code which implements: {request.prompt}"
        generated_tests = tester_agent.generate(generated_code, test_requirements)
        current_tests = generated_tests
        
        conversation_manager.add_message(
            role="tester",
            content=generated_tests,
            agent_type="tester"
        )
        
        history = conversation_manager.get_history()
        messages = [
            Message(
                role=msg["role"],
                content=msg["content"],
                agent_type=msg.get("agent_type"),
                timestamp=msg.get("timestamp")
            )
            for msg in history
        ]
        
        return GenerateResponse(
            status="success",
            code=generated_code,
            tests=generated_tests,
            conversation=messages
        )
    
    except Exception as e:
        conversation_manager.add_message(
            role="system",
            content=f"Error: {str(e)}",
            agent_type="system"
        )
        
        history = conversation_manager.get_history()
        messages = [
            Message(
                role=msg["role"],
                content=msg["content"],
                agent_type=msg.get("agent_type"),
                timestamp=msg.get("timestamp")
            )
            for msg in history
        ]
        
        return GenerateResponse(
            status="error",
            code=f"# Error: {str(e)}",
            tests=f"# Error: {str(e)}",
            conversation=messages
        )


@app.post("/execute")
async def execute(request: ExecuteRequest) -> dict:
    """Execute code and tests with feedback loop"""
    global current_code, current_tests
    try:
        current_code = request.code
        current_tests = request.tests
        
        full_test_code = f"{request.code}\n\n{request.tests}"
        
        execution_result = code_executor.execute(full_test_code, test_mode=True)
        
        if execution_result["status"] == "timeout":
            return {
                "status": "error",
                "execution_status": "timeout",
                "output": "",
                "error": execution_result["stderr"],
                "test_summary": "Execution timed out",
                "total_tests": 0,
                "passed_tests": 0,
                "failed_tests": 0,
                "test_details": [],
                "raw_output": execution_result["stderr"]
            }
        
        if execution_result["status"] == "error":
            return {
                "status": "error",
                "execution_status": "error",
                "output": execution_result["stdout"],
                "error": execution_result["stderr"],
                "test_summary": "Execution error",
                "total_tests": 0,
                "passed_tests": 0,
                "failed_tests": 0,
                "test_details": [],
                "raw_output": execution_result["stderr"]
            }
        
        parsed_results = ResultParser.parse_test_results(
            execution_result["stdout"] + execution_result["stderr"],
            execution_result["returncode"]
        )
        
        test_details = [
            {
                "name": detail["name"],
                "status": detail["status"],
                "params": detail.get("params", "")
            }
            for detail in parsed_results["test_details"]
        ]
        
        response = {
            "status": "success" if parsed_results["status"] == "passed" else "failed",
            "execution_status": parsed_results["status"],
            "output": execution_result["stdout"],
            "error": execution_result["stderr"],
            "test_summary": parsed_results["summary"],
            "total_tests": parsed_results["total"],
            "passed_tests": parsed_results["passed"],
            "failed_tests": parsed_results["failed"],
            "test_details": test_details,
            "raw_output": execution_result["stdout"] + execution_result["stderr"]
        }
        
        if ResultParser.should_retry(parsed_results) and current_prompt:
            feedback_message = f"Tests failed:\n{parsed_results['summary']}\n\nOriginal code:\n{request.code}\n\nFailing tests:\n{request.tests}\n\nPlease fix the code to pass all tests."
            
            conversation_manager.add_message(
                role="system",
                content="Tests failed. Tester agent is debugging...",
                agent_type="system"
            )
            
            refined_tests = tester_agent.generate(request.code, feedback_message)
            current_tests = refined_tests
            
            conversation_manager.add_message(
                role="tester",
                content=f"Refined tests after feedback:\n{refined_tests}",
                agent_type="tester"
            )
        
        return response
    
    except Exception as e:
        return {
            "status": "error",
            "execution_status": "error",
            "output": "",
            "error": str(e),
            "test_summary": "Error during execution",
            "total_tests": 0,
            "passed_tests": 0,
            "failed_tests": 0,
            "test_details": [],
            "raw_output": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)