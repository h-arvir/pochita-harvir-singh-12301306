import json
from agents.documentation import DocumentationAgent
from dotenv import load_dotenv

load_dotenv()

agent = DocumentationAgent()

code = """
def fibonacci(n):
    '''Generate fibonacci sequence'''
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def is_prime(num):
    '''Check if number is prime'''
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
"""

print("Testing DocumentationAgent...")
print("=" * 50)

result = agent.generate(code, "Math utility functions")

print(f"Status: {result['status']}")
print(f"Has documentation: {'documentation' in result}")

if result['status'] == 'success':
    doc = result['documentation']
    print(f"Overview: {doc.get('overview', 'N/A')[:80]}...")
    print(f"Usage examples: {len(doc.get('usage_examples', []))}")
    print(f"Components: {len(doc.get('architecture', {}).get('components', []))}")
    print("\n✓ Documentation generated successfully!")
else:
    print(f"Error: {result['documentation']['overview'][:100]}...")

print("\nSample markdown output:")
print("=" * 50)
markdown = agent.format_documentation_as_markdown(result)
print(markdown[:300] + "...")
