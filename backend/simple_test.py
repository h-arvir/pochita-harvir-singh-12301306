#!/usr/bin/env python
import sys
print("Python version:", sys.version)
print("Testing imports...")

try:
    from dotenv import load_dotenv
    print("✓ dotenv imported")
    load_dotenv()
except Exception as e:
    print(f"✗ dotenv error: {e}")
    sys.exit(1)

try:
    import google.generativeai as genai
    print("✓ google.generativeai imported")
except Exception as e:
    print(f"✗ google.generativeai error: {e}")
    sys.exit(1)

try:
    from agents.documentation import DocumentationAgent
    print("✓ DocumentationAgent imported")
except Exception as e:
    print(f"✗ DocumentationAgent import error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nAll imports successful!")
