"""
Pochita Backend - FastAPI Application
AI agents for collaborative code generation and testing
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

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


# Request/Response Models
class GenerateRequest(BaseModel):
    prompt: str
    description: str = ""


class GenerateResponse(BaseModel):
    status: str
    message: str


# Health Check Endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running"""
    return {
        "status": "healthy",
        "message": "Pochita API is running",
        "gemini_configured": bool(os.getenv("GEMINI_API_KEY"))
    }


# Placeholder endpoints (to be implemented in afternoon)
@app.post("/generate")
async def generate(request: GenerateRequest):
    """Generate code using AI agents"""
    return {
        "status": "not_implemented",
        "message": "Generate endpoint coming in Day 1 Afternoon"
    }


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