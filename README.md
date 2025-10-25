# Pochita - AI Code Generation & Testing Platform

A 36-hour hackathon project where 2 AI agents collaborate to generate and test Python code.

## Quick Start

### Backend
```bash
cd backend
python -m venv venv
# Activate venv (see SETUP.md for OS-specific commands)
pip install -r requirements.txt
# Add your OpenAI API key to .env
python main.py
```

**API runs at**: http://localhost:8000  
**Health check**: http://localhost:8000/health  
**API docs**: http://localhost:8000/docs

### Frontend (Coming in Day 1 Evening)
```bash
cd frontend
npm install
npm run dev
```

## Architecture

```
pochita/
├── backend/           # Python + FastAPI
│   ├── agents/       # Coder, Tester, Executor agents
│   ├── main.py       # FastAPI server
│   └── generated_code/  # Output directory
└── frontend/         # React + Vite
    └── src/
        ├── pages/
        └── App.jsx
```

## Project Timeline

- **Day 1 Morning** ✅ Setup & Planning
  - [x] Project structure
  - [x] FastAPI server with `/health` endpoint
  - [x] Agent boilerplates
  - [x] Environment setup

- **Day 1 Afternoon** ✅ Core Backend
  - [x] Implement `/generate` endpoint
  - [x] Coder & Tester agent logic

- **Day 1 Evening** ✅ Frontend & Integration
  - [x] React + Chakra UI setup
  - [x] Chat interface
  - [x] Backend integration

- **Day 2 Morning** ⏳ Code Execution & Polish
  - [ ] Implement `/execute` endpoint
  - [ ] Test result parsing

- **Day 2 Afternoon** ⏳ Demo Prep
  - [ ] End-to-end testing
  - [ ] Bug fixes
  - [ ] Demo preparation

## API Endpoints

| Method | Endpoint | Status | Description |
|--------|----------|--------|-------------|
| GET | `/health` | ✅ Ready | Health check |
| POST | `/generate` | 🔄 In Progress | Generate code & tests |
| POST | `/execute` | ⏳ TODO | Execute generated code |

## Documentation

- [Backend Setup](./backend/SETUP.md)
- [Project Plan](./plan.md)

## Success Criteria

✅ Agents generate valid Python code  
✅ Tests actually run and show results  
✅ User sees agent conversation in UI  
✅ System handles errors gracefully  
✅ Demo takes < 5 minutes

---

**Current Phase**: Day 1 Evening - Frontend & Integration ✅