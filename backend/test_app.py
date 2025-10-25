import traceback
import os
from dotenv import load_dotenv

load_dotenv()

try:
    print("Importing FastAPI...")
    from fastapi import FastAPI
    print("✓ FastAPI imported")
    
    print("Importing agents...")
    from agents.coder import CoderAgent
    print("✓ CoderAgent imported")
    
    from agents.tester import TesterAgent
    print("✓ TesterAgent imported")
    
    from agents.conversation_manager import ConversationManager
    print("✓ ConversationManager imported")
    
    from agents.executor import CodeExecutor
    print("✓ CodeExecutor imported")
    
    print("\nInitializing agents...")
    coder_agent = CoderAgent()
    print("✓ CoderAgent initialized")
    
    tester_agent = TesterAgent()
    print("✓ TesterAgent initialized")
    
    conversation_manager = ConversationManager()
    print("✓ ConversationManager initialized")
    
    print("\n✅ All imports and initialization successful!")
    
except Exception as e:
    print("\n❌ Error occurred:")
    traceback.print_exc()
