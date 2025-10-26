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

## Project Impact
Pochita addresses critical inefficiencies in the software development lifecycle:

- **Accelerated Development**: Reduces code boilerplate writing time by 60-80%, allowing developers to focus on architecture and business logic rather than repetitive coding tasks
- **Quality Assurance**: Automatically generates comprehensive test suites, improving code coverage and reducing bug escape rates
- **Learning Tool**: Serves as an interactive learning platform for junior developers to understand architectural patterns and testing best practices
- **Rapid Prototyping**: Enables quick prototyping and validation of ideas with AI-assisted code generation
- **Accessibility**: Democratizes code generation, making professional-grade code structure and testing accessible to developers of varying skill levels
- **Error Reduction**: Minimizes human error in test case creation and boilerplate code patterns
- **Productivity Gain**: Teams can deliver features faster while maintaining code quality and comprehensive test coverage

Pochita demonstrates the practical application of AI agents in automating complex, multi-stage software engineering workflows, showcasing the potential for AI to augment developer productivity in real-world scenarios.

---

## Tech Stack
- **Backend**: Python 3.13.7, FastAPI 0.104.1, Uvicorn 0.24.0
- **Frontend**: React 19.2.0, Vite 7.1.12, JavaScript
- **AI/LLM**: Google Generative AI (Gemini) - Multi-agent architecture with context window up to 100K tokens
- **Testing Framework**: pytest 7.4.3
- **Package Manager**: pip (Backend), npm (Frontend)
- **Web Framework**: FastAPI with CORS support
- **Schema Validation**: Pydantic ≥2.5.0
- **Cloud Deployment**: Vercel (Frontend), Render/Railway (Backend)
- **Version Control**: Git + GitHub
- **Agent Communication**: Conversation pipeline with multi-stage prompting

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

## LLM Choice & Model Documentation

### Selected Model: Google Gemini

**Model**: Google Generative AI - Gemini (default gemini-pro or gemini-1.5)

**Rationale for Selection**:
- **Free Tier Access**: Provides generous free API quota suitable for hackathon development and testing (15 requests per minute for free tier)
- **Multi-Agent Support**: Gemini's context window (up to 32K-100K tokens) enables multiple sequential prompts without losing conversation context, essential for the architect → coder → tester pipeline
- **Code Generation Capability**: Extensively trained on code from GitHub and Stack Overflow, making it highly proficient at generating Python code and pytest test cases
- **Availability**: Reliable API with minimal setup complexity using the `google-generativeai` Python SDK
- **Performance**: Fast response times suitable for real-time web interface interaction

### Sources & Documentation
- [Google AI Studio](https://aistudio.google.com/app/apikey) - API key generation and playground
- [Google Generative AI Python SDK](https://ai.google.dev/docs) - Official SDK documentation
- [Gemini Model Documentation](https://ai.google.dev/models/gemini) - Model specifications and capabilities
- [Google AI for Developers](https://ai.google.dev/) - Comprehensive API documentation

### Model Capabilities
- **Code Generation**: Proficient in generating Python functions, classes, and complete modules
- **Test Case Creation**: Strong ability to create comprehensive pytest test suites with multiple test cases
- **Architecture Analysis**: Can analyze requirements and produce architectural design documents
- **Context Retention**: Maintains conversation history across multiple API calls within session
- **Error Handling**: Provides meaningful error messages and explanations for failed code

### Limitations & Constraints

#### API-Level Limitations
- **Rate Limiting**: Free tier limited to ~15 requests/minute; production requires paid tier for higher throughput
- **Token Limits**: Maximum context window of 32K-100K tokens depending on model version (approximately 8,000-25,000 words per request)
- **Response Size**: Generated code/tests limited by token budget; very large applications may need to be generated in multiple parts
- **No Persistent Memory**: Each API session is independent; conversation history must be maintained in application state

#### Code Generation Limitations
- **Language Support**: Primarily optimized for Python; other languages work but with lower quality
- **Complex Architectures**: May struggle with highly complex enterprise-level architectural patterns
- **Database Queries**: Generated database code may not be production-optimized for large-scale data operations
- **Security Considerations**: Generated code should be reviewed for security vulnerabilities before production deployment
- **Dependencies**: May reference external libraries; generated code requires validation that dependencies are available
- **Edge Cases**: May miss handling of rare edge cases or unusual error scenarios

#### Hallucination & Accuracy Issues
- **Outdated Information**: Training data has a cutoff date; may generate code using deprecated APIs or outdated patterns
- **Fictitious Libraries**: Occasionally invents function names or library methods that don't exist
- **Logic Errors**: Can produce syntactically correct but logically flawed code
- **Test Coverage Gaps**: Generated tests may not cover all edge cases or failure scenarios

#### Performance Considerations
- **API Latency**: Network latency varies (typically 1-5 seconds per request)
- **Concurrent Requests**: Free tier has rate limits; production deployment requires payment tier
- **Token Consumption**: Large prompts consume tokens quickly; cost scales with input/output size

### Recommendations for Production Use
1. **API Key Management**: Use environment variables and never commit API keys to version control
2. **Code Review**: Always review generated code before production deployment
3. **Security Audit**: Run security scanners on generated code (e.g., Bandit for Python)
4. **Dependency Validation**: Verify all referenced libraries exist and are compatible with your environment
5. **Testing**: Treat generated tests as starting points; add domain-specific test cases
6. **Error Handling**: Implement comprehensive error handling for API failures and timeouts
7. **Paid Tier**: For production use, migrate to Google Cloud paid tier for higher rate limits and SLAs

### Alternative Models Considered
- **OpenAI GPT-4**: Superior code generation but requires paid API; higher latency
- **Anthropic Claude**: Excellent code quality but less generous free tier
- **Open Source Models (Llama, CodeLlama)**: Would require hosting infrastructure; not practical for hackathon timeline

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

### AI/LLM Resources
- [Google AI for Developers](https://ai.google.dev/) - Official Gemini API documentation and developer guides
- [Google Generative AI Python SDK](https://ai.google.dev/docs) - Python SDK for Gemini models
- [Google AI Studio](https://aistudio.google.com/app/apikey) - Interactive playground and API key management
- [Gemini Models Documentation](https://ai.google.dev/models/gemini) - Model specifications, capabilities, and context windows
- [Google Cloud Generative AI Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini) - Production deployment guides

### Framework & Library Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Modern web framework for building APIs
- [React Documentation](https://react.dev/) - UI library for building interactive interfaces
- [Vite Documentation](https://vitejs.dev/) - Next-generation frontend build tool
- [pytest Documentation](https://docs.pytest.org/) - Python testing framework
- [Pydantic Documentation](https://docs.pydantic.dev/) - Data validation using Python type annotations

### Related Tools & Comparisons
- [OpenAI GPT Models](https://platform.openai.com/docs/models) - Alternative LLM provider
- [Anthropic Claude Documentation](https://www.anthropic.com/claude) - Alternative LLM provider
- [Hugging Face Models](https://huggingface.co/models) - Open-source model hub
- [Code Quality Tools - Bandit](https://bandit.readthedocs.io/en/latest/) - Python security linter for generated code review
---

## Acknowledgements
Built as a 36-hour hackathon project leveraging:
- **Google Generative AI / Gemini** for intelligent code generation and multi-agent collaboration ([Gemini API](https://ai.google.dev/))
- **FastAPI** for robust backend architecture ([FastAPI Framework](https://fastapi.tiangolo.com/))
- **React & Vite** for modern frontend development ([React 19](https://react.dev/), [Vite](https://vitejs.dev/))
- **pytest** for automated testing framework ([pytest](https://docs.pytest.org/))
- **Pydantic** for data validation ([Pydantic](https://docs.pydantic.dev/))
- Open-source Python and JavaScript ecosystems

### External Model Citation
This project uses **Google Generative AI (Gemini)** as its primary language model for code generation and analysis. The Gemini model is:
- Developed and maintained by Google DeepMind
- Accessed via the [Google AI API](https://ai.google.dev/)
- Subject to [Google's Terms of Service](https://policies.google.com/terms) and [Privacy Policy](https://policies.google.com/privacy)
- Free tier includes 15 requests/minute with rate limiting; production deployment requires a paid Google Cloud account

For academic or commercial use, please refer to [Google's AI Principles](https://ai.google/principles/) and licensing terms.

