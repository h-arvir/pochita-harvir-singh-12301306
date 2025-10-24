"""
Coder Agent - Generates Python code using LangChain and Gemini
Custom logic for code validation and formatting
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import GooglePalm
import os


class CoderAgent:
    """Agent responsible for generating Python code"""
    
    def __init__(self):
        self.llm = GooglePalm(
            temperature=0.7,
            google_api_key=os.getenv("GEMINI_API_KEY")
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["request"],
            template="""You are an expert Python developer. Generate clean, well-documented Python code.

User Request: {request}

Requirements:
- Write valid, executable Python code
- Include docstring with description
- Add type hints where applicable
- Make the code modular and reusable

Generate ONLY the Python code, no explanations:"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def generate(self, request: str) -> str:
        """Generate code based on user request"""
        try:
            code = self.chain.run(request=request)
            return self._validate_code(code)
        except Exception as e:
            return f"Error generating code: {str(e)}"
    
    def _validate_code(self, code: str) -> str:
        """Validate generated code format"""
        code = code.strip()
        if not code:
            return "# Error: No code generated"
        return code