"""
Pochita Backend - FastAPI Application
AI agents for collaborative code generation and testing
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from typing import List, Dict

from agents.coder import CoderAgent
from agents.tester import TesterAgent
from agents.conversation_manager import ConversationManager
from agents.executor import CodeExecutor

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
coder_agent = CoderAgent()
tester_agent = TesterAgent()
conversation_manager = ConversationManager()


# Request/Response Models
class GenerateRequest(BaseModel):
    prompt: str
    description: str = ""


class Message(BaseModel):
    role: str
    content: str
    agent_type: str = None
    timestamp: str = None


class GenerateResponse(BaseModel):
    status: str
    code: str
    tests: str
    conversation: List[Message]


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
    try:
        conversation_manager.clear()
        
        conversation_manager.add_message(
            role="user",
            content=request.prompt,
            agent_type="user"
        )
        
        coder_prompt = f"{request.prompt}\n\nAdditional context: {request.description}" if request.description else request.prompt
        
        conversation_manager.add_message(
            role="system",
            content="Coder agent is generating code...",
            agent_type="system"
        )
        
        generated_code = coder_agent.generate(coder_prompt)
        
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
async def execute(code: str):
    """Execute generated code"""
    return {
        "status": "not_implemented",
        "message": "Execute endpoint coming in Day 2 Morning"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)