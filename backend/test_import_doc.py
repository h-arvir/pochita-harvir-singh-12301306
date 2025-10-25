import sys
import traceback

try:
    from agents.documentation import DocumentationAgent
    print("Import successful!")
    agent = DocumentationAgent()
    print("Initialization successful!")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
    sys.exit(1)
