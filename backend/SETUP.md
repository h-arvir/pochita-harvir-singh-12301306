# Backend Setup Instructions

## 1. Create Virtual Environment

```bash
cd backend
python -m venv venv
```

## 2. Activate Virtual Environment

### Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

### Windows (CMD):
```cmd
venv\Scripts\activate.bat
```

### macOS/Linux:
```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure OpenAI API Key

Create `.env` file in the `backend/` directory:

```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

**Get your API key from:** https://platform.openai.com/api-keys

## 5. Run FastAPI Server

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 6. Verify Server is Running

Visit: http://localhost:8000/health

Expected response:
```json
{
  "status": "healthy",
  "message": "Pochita API is running",
  "openai_configured": true
}
```

## 7. View API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Project Structure

```
backend/
├── venv/                      # Virtual environment (created after setup)
├── agents/
│   ├── __init__.py
│   ├── coder.py              # Coder agent for code generation
│   ├── tester.py             # Tester agent for test generation
│   ├── executor.py           # Code execution sandbox
│   └── conversation_manager.py  # Conversation tracking
├── generated_code/           # Output folder for generated code
├── main.py                   # FastAPI application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create this)
└── SETUP.md                  # This file
```

---

## Next Steps

- **Day 1 Afternoon**: Implement `/generate` endpoint with Coder and Tester agents
- **Day 2 Morning**: Implement `/execute` endpoint with code execution