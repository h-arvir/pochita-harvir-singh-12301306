# Pochita - AI Code Generation & Testing Platform

## Project Overview
Pochita is an intelligent code generation and testing platform that leverages AI agents to collaboratively generate Python code and comprehensive test suites from natural language prompts. Built during a 36-hour hackathon, it demonstrates seamless integration between multiple AI agents and a modern web interface.

---

## Problem Statement
Developers spend significant time writing boilerplate code and test suites from scratch. Even with code templates and frameworks, the process remains manual and error-prone. There's a need for an automated solution that can understand requirements in natural language and generate both production-ready code and comprehensive tests, reducing development time and ensuring code quality.

---

## Solution Summary
Pochita is an end-to-end web application that automates code generation and testing using three specialized AI agents:
- **Architect Agent**: Analyzes requirements and designs the solution architecture
- **Coder Agent**: Generates clean, production-ready Python code
- **Tester Agent**: Creates comprehensive test suites to validate the generated code

Users submit a natural language prompt through an intuitive web interface. The agents collaborate in a conversation pipeline, and the platform displays the generated code, tests, and execution results in a unified dashboard. Users can execute tests, review agent conversations, and download generated artifacts.

---

## Tech Stack
- **Backend**: Python 3.13.7, FastAPI 0.104.1, Uvicorn 0.24.0
- **Frontend**: React 19.2.0, Vite 7.1.12, JavaScript
- **AI/LLM**: Google Generative AI (Gemini)
- **Testing Framework**: pytest 7.4.3
- **Package Manager**: pip (Backend), npm (Frontend)
- **Web Framework**: FastAPI with CORS support
- **Schema Validation**: Pydantic ≥2.5.0
- **Cloud Deployment**: Vercel (Frontend), Render/Railway (Backend)
- **Version Control**: Git + GitHub

---

## Project Structure
```
pochita/
├── backend/                          # FastAPI backend
│   ├── agents/                       # AI agents for code generation
│   │   ├── architect.py              # Architecture analysis agent
│   │   ├── coder.py                  # Code generation agent
│   │   ├── tester.py                 # Test generation agent
│   │   ├── executor.py               # Code execution engine
│   │   ├── result_parser.py          # Parse test execution results
│   │   ├── conversation_manager.py   # Manage agent conversations
│   │   └── __init__.py
│   ├── generated_code/               # Output directory for generated files
│   ├── main.py                       # FastAPI application entry point
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                  # Environment variables template
│   └── .gitignore
├── frontend/                         # React + Vite frontend
│   ├── src/
│   │   ├── components/               # React components
│   │   │   ├── ChatInterface.jsx     # Display agent conversations
│   │   │   ├── CodeDisplay.jsx       # Show generated code/tests
│   │   │   ├── ArchitectDisplay.jsx  # Show architecture analysis
│   │   │   ├── TestResults.jsx       # Display test execution results
│   │   │   └── App.jsx               # Main application component
│   │   ├── App.css                   # Application styling
│   │   └── main.jsx                  # React entry point
│   ├── dist/                         # Build output
│   ├── package.json                  # Node.js dependencies
│   ├── vite.config.js                # Vite configuration
│   ├── index.html                    # HTML template
│   ├── .env.example                  # Environment variables template
│   └── package-lock.json
├── .env.example                      # Root environment template
├── vercel.json                       # Vercel deployment config
├── Procfile                          # Heroku/Render deployment config
├── README.md                         # This file
└── .gitignore
```

---

## Setup Instructions

### Prerequisites
- **Python**: 3.13.7 or higher
- **Node.js**: 18+ and npm
- **Git**: For version control

### Backend Setup
```bash
# 1. Navigate to backend directory
cd backend

# 2. Create and activate a Python virtual environment
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Create a .env file in the backend/ directory
cp .env.example .env
# Add your GEMINI_API_KEY to .env
# GEMINI_API_KEY=your_api_key_here

# 5. Start the FastAPI server
python main.py
# Server runs on http://localhost:8000
```

### Frontend Setup
```bash
# 1. Navigate to frontend directory
cd frontend

# 2. Install Node.js dependencies
npm install

# 3. Configure environment variables (optional)
# By default, frontend connects to http://localhost:8000
cp .env.example .env
# Set VITE_API_URL if connecting to a different backend

# 4. Start the development server
npm run dev
# Frontend runs on http://localhost:5173
```

---

## Features
- **Multi-Agent Collaboration**: Architect, Coder, and Tester agents work together to generate production-ready code and comprehensive tests
- **Real-time Agent Conversations**: View the entire conversation flow between agents during code generation
- **Automated Test Generation**: Pytest-based test suites are automatically generated alongside code
- **Test Execution & Feedback Loop**: Run tests directly from the web interface and view detailed results
- **Code Export**: Download generated code and tests as a ZIP file
- **Interactive UI**: Clean, intuitive interface with tab-based navigation
- **Conversation Transparency**: See exactly how each agent analyzes and processes your requirements
- **Error Handling**: Robust error handling with graceful failure messages and timeout protection

---


---

## Deployment

### Frontend Deployment (Vercel)
```bash
cd frontend
npm run build
# Deploy the dist/ directory to Vercel
# Set VITE_API_URL environment variable in Vercel dashboard
```

### Backend Deployment (Render/Railway)
1. Push code to GitHub
2. Connect repository to Render/Railway
3. Set environment variables:
   - `GEMINI_API_KEY`: Your Google Generative AI API key
   - `PORT`: 8000 (or desired port)
4. Deploy with `python main.py` as the start command

### Live Demo URL : 

https://pochita-eight.vercel.app/

---

## Demo Video
*(Add your demo video link here)*

The demo should showcase:
- Entering a code generation prompt
- Viewing agent architecture analysis
- Generated code and tests
- Running tests and viewing results
- Agent conversation flow
- Code download functionality

---

## How It Works
1. **User Input**: User enters a natural language prompt describing the code they want generated
2. **Architect Analysis**: Architect agent analyzes requirements and designs a solution approach
3. **Code Generation**: Coder agent generates Python code based on the architecture
4. **Test Generation**: Tester agent creates comprehensive pytest test suites
5. **Display & Execution**: Generated code and tests are displayed in the UI, ready for execution
6. **Test Feedback**: Tests can be executed directly, showing pass/fail results
7. **Artifact Export**: Users can download generated code and tests as ZIP files

---

## Environment Variables

### Backend (.env)
```
GEMINI_API_KEY=your_google_ai_api_key_here
PORT=8000
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000
```

---

## Technologies & Libraries

### Python Backend
- **FastAPI**: Modern web framework for building APIs
- **google-generativeai**: Google Generative AI client for Gemini models
- **pytest**: Testing framework for Python
- **pydantic**: Data validation using Python type annotations
- **python-dotenv**: Environment variable management
- **uvicorn**: ASGI web server

### React Frontend
- **React 19**: UI library for building interactive components
- **Vite**: Next-generation frontend build tool
- **JSZip**: ZIP file generation in the browser

---

## Development Workflow
1. Clone the repository
2. Set up backend with virtual environment and API key
3. Set up frontend with npm dependencies
4. Run both servers concurrently (one in each terminal)
5. Navigate to http://localhost:5173 to test
6. Make changes, restart servers as needed
7. Run backend tests before committing: `pytest`

---

## Future Enhancements
- agents like Code-correction when a test case fails and github-integration to push/pull code from github
- Support for multiple programming languages (JavaScript, Java, etc.)
- Persistent storage of generated code history
- User authentication and project management
- Advanced code optimization suggestions
- Integration with GitHub for direct commits
- Real-time collaboration features
- Custom model selection
- Performance benchmarking and metrics

---

## Troubleshooting

### Backend Issues
- **Module not found**: Ensure virtual environment is activated and all dependencies installed
- **API key error**: Verify GEMINI_API_KEY is set in .env file
- **CORS errors**: Frontend may be on wrong domain; check VITE_API_URL configuration

### Frontend Issues
- **Cannot connect to backend**: Ensure backend is running on http://localhost:8000
- **API calls failing**: Check browser console for detailed error messages
- **Port already in use**: Kill existing processes or change port configuration


---

## References & Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Google Generative AI Python SDK](https://ai.google.dev/docs)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [pytest Documentation](https://docs.pytest.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Chatgpt](https://chatgpt.com/)
- [Gemini](https://gemini.google.com/app)
---

## Acknowledgements
Built as a 36-hour hackathon project leveraging:
- Google Generative AI / Gemini for intelligent code generation
- FastAPI for robust backend architecture
- React & Vite for modern frontend development
- pytest for testing framework
- Open-source Python and JavaScript ecosystems

