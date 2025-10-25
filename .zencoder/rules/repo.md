---
description: Repository Information Overview
alwaysApply: true
---

# Pochita Information

## Summary
Pochita is an AI Code Generation & Testing Platform developed during a 36-hour hackathon. It features two AI agents that collaborate to generate and test Python code based on user prompts.

## Structure
- **backend/**: Python FastAPI server with AI agents
  - **agents/**: Contains coder, tester, executor agents
  - **generated_code/**: Output directory for generated code
- **frontend/**: React + Vite web interface
  - **src/**: React components and application logic

## Language & Runtime
**Language**: Python 3.13.7 (Backend), JavaScript/React 19 (Frontend)
**Build System**: Python modules (Backend), Vite (Frontend)
**Package Manager**: pip (Backend), npm (Frontend)

## Dependencies
**Backend Dependencies**:
- fastapi==0.104.1
- uvicorn==0.24.0
- google-generativeai>=0.5.0
- python-dotenv==1.0.0
- pydantic>=2.5.0
- pytest==7.4.3

**Frontend Dependencies**:
- react==19.2.0
- react-dom==19.2.0
- vite==7.1.12 (dev)

## Build & Installation
**Backend**:
```bash
cd backend
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
# Add GEMINI_API_KEY to .env
python main.py
```

**Frontend**:
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints
- **GET /health**: Health check endpoint
- **POST /generate**: Generate code and tests using AI agents
- **POST /execute**: Execute generated code and tests

## Testing
**Framework**: pytest
**Test Location**: Backend tests in test_app.py
**Run Command**:
```bash
cd backend
pytest
```

## Projects

### Backend (FastAPI)
**Configuration File**: requirements.txt

#### Components
- **CoderAgent**: Generates code based on user prompts
- **TesterAgent**: Creates tests for the generated code
- **CodeExecutor**: Executes the code and tests
- **ResultParser**: Parses test execution results
- **ConversationManager**: Tracks agent conversation

#### Main Entry Point
The main.py file starts the FastAPI server with uvicorn on port 8000.

### Frontend (React)
**Configuration File**: package.json

#### Components
- **App.jsx**: Main application component
- **ChatInterface**: Displays agent conversation
- **CodeDisplay**: Shows generated code and tests
- **TestResults**: Displays test execution results

#### Main Entry Point
The main.jsx file renders the React application.