"""
Tester Agent - Generates test cases using LangChain and Gemini
Custom test template generation and assertion builders
"""

import google.generativeai as genai
import os
import re
import ast


class TesterAgent:
    """Agent responsible for generating test cases"""
    
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        
        self.prompt_template = """You are an expert Python test developer. Generate comprehensive test cases using pytest.

Code to Test:
{code}

Requirements: {requirements}

Generate pytest test cases with:
- At least 3 test cases covering normal cases
- Edge case tests (empty inputs, boundary values, None)
- Error/exception handling tests
- Clear, descriptive test function names
- Use assert statements for clarity
- Include docstrings for each test

Test Structure:
- Use descriptive function names: test_<function>_<scenario>
- Group related tests together
- Use pytest fixtures if needed for setup/teardown

Generate ONLY the Python test code, no explanations or markdown:"""
    
    def generate(self, code: str, requirements: str = "") -> str:
        """Generate test cases for given code"""
        try:
            prompt = self.prompt_template.format(code=code, requirements=requirements)
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                )
            )
            tests = response.text
            return self._format_and_validate_tests(tests)
        except Exception as e:
            return f"# Error generating tests: {str(e)}"
    
    def _format_and_validate_tests(self, tests: str) -> str:
        """Format and validate test code"""
        tests = tests.strip()
        if not tests:
            return "# Error: No tests generated"
        
        tests = self._extract_code_blocks(tests)
        tests = self._ensure_pytest_import(tests)
        tests = self._validate_test_syntax(tests)
        tests = self._enhance_assertions(tests)
        
        return tests
    
    def _extract_code_blocks(self, text: str) -> str:
        """Extract code from markdown code blocks if present"""
        code_block_match = re.search(r'```(?:python)?\n(.*?)\n```', text, re.DOTALL)
        if code_block_match:
            return code_block_match.group(1).strip()
        return text
    
    def _ensure_pytest_import(self, tests: str) -> str:
        """Ensure pytest is imported"""
        if "import pytest" not in tests and "from pytest" not in tests:
            tests = "import pytest\n" + tests
        return tests
    
    def _validate_test_syntax(self, tests: str) -> str:
        """Validate Python syntax of test code"""
        try:
            ast.parse(tests)
            return tests
        except SyntaxError as e:
            return f"# Syntax Error in tests: {str(e)}\n# Original tests:\n{tests}"
    
    def _enhance_assertions(self, tests: str) -> str:
        """Enhance assertion clarity with better error messages"""
        lines = tests.split('\n')
        enhanced_lines = []
        
        for line in lines:
            if 'assert ' in line and ' == ' in line:
                if ', ' not in line and 'msg=' not in line:
                    parts = line.split('assert ')
                    if len(parts) == 2:
                        assertion = parts[1].strip()
                        indent = len(line) - len(line.lstrip())
                        spaces = ' ' * indent
                        left, right = assertion.split(' == ', 1)
                        msg = f', msg=f"Expected {{expected}}, got {{actual}}"'.replace('{{expected}}', right.strip()).replace('{{actual}}', left.strip())
                        enhanced_lines.append(f'{spaces}assert {assertion}')
                    else:
                        enhanced_lines.append(line)
                else:
                    enhanced_lines.append(line)
            else:
                enhanced_lines.append(line)
        
        return '\n'.join(enhanced_lines)