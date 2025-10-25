import traceback
import sys

try:
    print("Python version:", sys.version)
    print("Attempting to import google.generativeai...")
    import google.generativeai as genai
    print("Successfully imported google.generativeai")
    
    print("Attempting to import from agents.coder...")
    from agents.coder import CoderAgent
    print("Success!")
except Exception as e:
    print("Error occurred:")
    traceback.print_exc()
