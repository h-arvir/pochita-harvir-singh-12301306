"""
Tester Agent - Generates test cases using LangChain and Gemini
Custom test template generation and assertion builders
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import GooglePalm
import os


class TesterAgent:
    """Agent responsible for generating test cases"""
    
    def __init__(self):
        self.llm = GooglePalm(
            temperature=0.7,
            google_api_key=os.getenv("GEMINI_API_KEY")
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["code", "requirements"],
            template="""You are an expert Python test developer. Generate comprehensive test cases.

Code to Test:
{code}

Requirements: {requirements}

Generate pytest test cases with:
- Multiple test cases covering normal cases
- Edge case handling
- Error handling tests
- Clear assertions

Generate ONLY the Python test code, no explanations:"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def generate(self, code: str, requirements: str = "") -> str:
        """Generate test cases for given code"""
        try:
            tests = self.chain.run(code=code, requirements=requirements)
            return self._format_tests(tests)
        except Exception as e:
            return f"# Error generating tests: {str(e)}"
    
    def _format_tests(self, tests: str) -> str:
        """Format and validate test code"""
        tests = tests.strip()
        if not tests:
            return "# Error: No tests generated"
        
        # Ensure pytest import
        if "import pytest" not in tests and "from pytest" not in tests:
            tests = "import pytest\n" + tests
        
        return tests