import asyncio
import json
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_documentation_generation():
    payload = {
        "prompt": "Create a function to calculate fibonacci numbers",
        "description": "A simple fibonacci sequence generator"
    }
    
    response = client.post("/generate", json=payload)
    print("Status Code:", response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        print("\nResponse Keys:", list(data.keys()))
        print("Status:", data.get("status"))
        print("Code Generated:", "Yes" if data.get("code") else "No")
        print("Tests Generated:", "Yes" if data.get("tests") else "No")
        print("Documentation:", "Yes" if data.get("documentation") else "No")
        print("Documentation Markdown:", "Yes" if data.get("documentation_markdown") else "No")
        
        if data.get("documentation"):
            doc = data["documentation"]
            print("\nDocumentation Structure:")
            print("- Overview:", bool(doc.get("overview")))
            print("- Usage Examples:", len(doc.get("usage_examples", [])))
            print("- Installation:", bool(doc.get("installation")))
            print("- Dependencies:", len(doc.get("dependencies", [])))
            print("- Configuration:", bool(doc.get("configuration")))
            print("- Running Locally:", bool(doc.get("running_locally")))
            print("- Architecture:", bool(doc.get("architecture")))
            
            if doc.get("overview"):
                print("\nOverview:", doc["overview"][:100], "...")
        else:
            print("\nNo documentation in response!")
            print("Full response:", json.dumps(data, indent=2)[:500])
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    test_documentation_generation()
