"""
Coder Agent - Generates Python code using LangChain and Gemini
Custom logic for code validation and formatting
"""

import google.generativeai as genai
import os
import ast
import re


class CoderAgent:
    """Agent responsible for generating Python code"""
    
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        
        self.prompt_template = """You are an expert Python developer. Generate clean, well-documented Python code.

User Request: {request}

Requirements:
- Write valid, executable Python code
- Include docstring with description
- Add type hints where applicable
- Make the code modular and reusable
- Format code with proper indentation
- Include meaningful variable names

Generate ONLY the Python code, no explanations:"""
    
    def generate(self, request: str) -> str:
        """Generate code based on user request"""
        try:
            prompt = self.prompt_template.format(request=request)
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                )
            )
            code = response.text
            return self._validate_and_format_code(code)
        except Exception as e:
            return f"# Error generating code: {str(e)}"
    
    def _validate_and_format_code(self, code: str) -> str:
        """Validate and format generated code"""
        code = code.strip()
        if not code:
            return "# Error: No code generated"
        
        code = self._extract_code_blocks(code)
        code = self._validate_syntax(code)
        code = self._ensure_imports(code)
        
        return code
    
    def _extract_code_blocks(self, text: str) -> str:
        """Extract code from markdown code blocks if present"""
        code_block_match = re.search(r'```(?:python)?\n(.*?)\n```', text, re.DOTALL)
        if code_block_match:
            return code_block_match.group(1).strip()
        return text
    
    def _validate_syntax(self, code: str) -> str:
        """Validate Python syntax and return code or error message"""
        try:
            ast.parse(code)
            return code
        except SyntaxError as e:
            return f"# Syntax Error: {str(e)}\n# Original code:\n{code}"
    
    def _ensure_imports(self, code: str) -> str:
        """Ensure necessary imports are present based on code content"""
        if 'datetime' in code and 'import datetime' not in code and 'from datetime' not in code:
            code = 'from datetime import datetime\n' + code
        
        if 're.' in code and 'import re' not in code:
            code = 'import re\n' + code
        
        if 'json.' in code and 'import json' not in code:
            code = 'import json\n' + code
        
        return code