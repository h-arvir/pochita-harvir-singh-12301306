"""
Documentation Agent - Generates comprehensive documentation for generated code
Creates usage examples, architecture diagrams, installation instructions, and configuration guides
"""

import google.generativeai as genai
import os
import json


class DocumentationAgent:
    """Agent responsible for generating comprehensive documentation"""
    
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        
        self.prompt_template = """You are an expert technical documentation writer. Generate comprehensive documentation for the following Python code.

User Request: {request}

Code to Document:
{code}

Generate documentation in structured format (valid JSON) with the following sections:

{{
    "overview": "Brief description of what this code does",
    
    "usage_examples": [
        {{
            "title": "Basic Usage",
            "code": "# Python code example",
            "description": "What this example demonstrates"
        }},
        {{
            "title": "Advanced Usage",
            "code": "# Python code example",
            "description": "What this example demonstrates"
        }}
    ],
    
    "installation": {{
        "requirements": ["Python 3.8+", "Any specific libraries"],
        "steps": [
            "Step 1: Description",
            "Step 2: Description"
        ]
    }},
    
    "dependencies": [
        {{
            "name": "module_name",
            "version": "recommended version",
            "description": "What it does",
            "installation": "pip install command"
        }}
    ],
    
    "configuration": {{
        "environment_variables": [
            {{
                "name": "VARIABLE_NAME",
                "description": "What this variable does",
                "default": "default value if any",
                "required": true
            }}
        ],
        "config_file_example": "YAML or JSON configuration example",
        "settings": [
            {{
                "name": "Setting name",
                "type": "string|int|bool",
                "description": "What this setting does",
                "default": "default value"
            }}
        ]
    }},
    
    "running_locally": {{
        "prerequisites": ["List of required software"],
        "setup_steps": [
            "Step 1: Clone/setup",
            "Step 2: Install dependencies",
            "Step 3: Configure",
            "Step 4: Run"
        ],
        "verification": "How to verify it's working correctly"
    }},
    
    "architecture": {{
        "description": "High-level architecture overview",
        "components": [
            {{
                "name": "Component Name",
                "responsibility": "What this component does",
                "interactions": "How it interacts with other components"
            }}
        ],
        "ascii_diagram": "Simple ASCII art diagram of the architecture",
        "data_flow": "Description of data flow through the system"
    }}
}}

Requirements:
- Provide accurate, practical documentation
- Include code examples that are ready to run
- Be clear and concise in descriptions
- Generate ONLY valid JSON, no markdown or explanations
- Include realistic examples based on the code provided
- Ensure all sections are populated with relevant information
- Make ASCII diagrams simple but informative"""
    
    def generate(self, code: str, request: str = "") -> dict:
        """Generate comprehensive documentation for given code"""
        try:
            prompt = self.prompt_template.format(
                request=request or "Generated code documentation",
                code=code
            )
            
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        max_output_tokens=4096,
                    )
                )
                documentation_text = response.text
            except Exception as api_error:
                print(f"[ERROR] Gemini API call failed: {str(api_error)}")
                return self._generate_fallback_documentation(code, request)
            
            result = self._parse_and_validate_documentation(documentation_text)
            return result
        except Exception as e:
            import traceback
            error_msg = f"Error generating documentation: {str(e)}\n{traceback.format_exc()}"
            print(f"[ERROR] {error_msg}")
            return self._error_response(error_msg)
    
    def _parse_and_validate_documentation(self, response_text: str) -> dict:
        """Parse and validate the JSON documentation response"""
        try:
            if not response_text or not response_text.strip():
                return self._error_response("Empty response from documentation generator")
            
            clean_text = response_text.strip()
            
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.startswith("```"):
                clean_text = clean_text[3:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            
            clean_text = clean_text.strip()
            
            if not clean_text:
                return self._error_response("No JSON content found in response")
            
            documentation = json.loads(clean_text)
            
            self._validate_structure(documentation)
            
            return {
                "status": "success",
                "documentation": documentation
            }
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON in documentation: {str(e)}\nReceived: {response_text[:200]}"
            return self._error_response(error_msg)
        except Exception as e:
            import traceback
            error_msg = f"Error parsing documentation: {str(e)}\n{traceback.format_exc()}"
            return self._error_response(error_msg)
    
    def _validate_structure(self, doc: dict) -> None:
        """Validate that documentation has expected sections"""
        required_sections = [
            "overview",
            "usage_examples",
            "installation",
            "dependencies",
            "configuration",
            "running_locally",
            "architecture"
        ]
        
        for section in required_sections:
            if section not in doc:
                doc[section] = self._get_default_section(section)
    
    def _get_default_section(self, section: str) -> any:
        """Return default structure for missing sections"""
        defaults = {
            "overview": "No overview available",
            "usage_examples": [],
            "installation": {"requirements": [], "steps": []},
            "dependencies": [],
            "configuration": {"environment_variables": [], "config_file_example": "", "settings": []},
            "running_locally": {"prerequisites": [], "setup_steps": [], "verification": ""},
            "architecture": {"description": "", "components": [], "ascii_diagram": "", "data_flow": ""}
        }
        return defaults.get(section, {})
    
    def _generate_fallback_documentation(self, code: str, request: str) -> dict:
        """Generate basic documentation when AI fails"""
        import re
        
        functions = re.findall(r'def\s+(\w+)\s*\(', code)
        classes = re.findall(r'class\s+(\w+)', code)
        
        return {
            "status": "success",
            "documentation": {
                "overview": f"Auto-generated documentation for: {request or 'Generated code'}",
                "usage_examples": [
                    {
                        "title": "Basic Usage",
                        "code": code[:200] + "...",
                        "description": "Basic usage of the generated code"
                    }
                ],
                "installation": {
                    "requirements": ["Python 3.8+"],
                    "steps": [
                        "Copy the code to your project",
                        "Import the necessary modules",
                        "Use the code as needed"
                    ]
                },
                "dependencies": [],
                "configuration": {
                    "environment_variables": [],
                    "config_file_example": "# No configuration needed",
                    "settings": []
                },
                "running_locally": {
                    "prerequisites": ["Python 3.8+"],
                    "setup_steps": [
                        "Place the code file in your project",
                        "Import and use the functions/classes"
                    ],
                    "verification": "Run the code and verify the output"
                },
                "architecture": {
                    "description": "Simple standalone code implementation",
                    "components": [
                        {
                            "name": f"{func}()",
                            "responsibility": "Function implementation",
                            "interactions": "Direct function calls"
                        }
                        for func in functions[:3]
                    ] + [
                        {
                            "name": f"{cls} class",
                            "responsibility": "Class implementation",
                            "interactions": "Class instantiation and method calls"
                        }
                        for cls in classes[:3]
                    ],
                    "ascii_diagram": "code\n  |\n  v\noutput",
                    "data_flow": "Input -> Process -> Output"
                }
            }
        }
    
    def _error_response(self, error_msg: str) -> dict:
        """Return formatted error response"""
        return {
            "status": "error",
            "documentation": {
                "overview": error_msg,
                "usage_examples": [],
                "installation": {"requirements": [], "steps": []},
                "dependencies": [],
                "configuration": {"environment_variables": [], "config_file_example": "", "settings": []},
                "running_locally": {"prerequisites": [], "setup_steps": [], "verification": ""},
                "architecture": {"description": "", "components": [], "ascii_diagram": "", "data_flow": ""}
            }
        }
    
    def format_documentation_as_markdown(self, documentation: dict) -> str:
        """Convert documentation dictionary to readable markdown format"""
        try:
            md = []
            doc = documentation.get("documentation", {})
            
            md.append("# Documentation\n")
            
            if "overview" in doc:
                md.append(f"## Overview\n\n{doc['overview']}\n")
            
            if "usage_examples" in doc and doc["usage_examples"]:
                md.append("## Usage Examples\n")
                for example in doc["usage_examples"]:
                    md.append(f"### {example.get('title', 'Example')}\n")
                    md.append(f"{example.get('description', '')}\n")
                    md.append(f"```python\n{example.get('code', '')}\n```\n")
            
            if "installation" in doc:
                inst = doc["installation"]
                md.append("## Installation\n")
                if inst.get("requirements"):
                    md.append("### Requirements\n")
                    for req in inst["requirements"]:
                        md.append(f"- {req}\n")
                if inst.get("steps"):
                    md.append("### Steps\n")
                    for i, step in enumerate(inst["steps"], 1):
                        md.append(f"{i}. {step}\n")
            
            if "dependencies" in doc and doc["dependencies"]:
                md.append("## Dependencies\n")
                for dep in doc["dependencies"]:
                    md.append(f"### {dep.get('name', 'Unknown')}\n")
                    md.append(f"- **Version**: {dep.get('version', 'N/A')}\n")
                    md.append(f"- **Description**: {dep.get('description', 'N/A')}\n")
                    md.append(f"- **Installation**: `{dep.get('installation', 'N/A')}`\n")
            
            if "configuration" in doc:
                config = doc["configuration"]
                md.append("## Configuration\n")
                if config.get("environment_variables"):
                    md.append("### Environment Variables\n")
                    for var in config["environment_variables"]:
                        required = "✓ Required" if var.get("required") else "Optional"
                        md.append(f"- **{var.get('name', 'UNKNOWN')}** [{required}]: {var.get('description', 'N/A')}\n")
                        if var.get("default"):
                            md.append(f"  - Default: `{var['default']}`\n")
                if config.get("config_file_example"):
                    md.append("### Configuration File Example\n")
                    md.append("```yaml\n")
                    md.append(config["config_file_example"])
                    md.append("\n```\n")
            
            if "running_locally" in doc:
                running = doc["running_locally"]
                md.append("## Running Locally\n")
                if running.get("prerequisites"):
                    md.append("### Prerequisites\n")
                    for prereq in running["prerequisites"]:
                        md.append(f"- {prereq}\n")
                if running.get("setup_steps"):
                    md.append("### Setup Steps\n")
                    for i, step in enumerate(running["setup_steps"], 1):
                        md.append(f"{i}. {step}\n")
                if running.get("verification"):
                    md.append(f"### Verification\n\n{running['verification']}\n")
            
            if "architecture" in doc:
                arch = doc["architecture"]
                md.append("## Architecture\n")
                if arch.get("description"):
                    md.append(f"{arch['description']}\n")
                if arch.get("ascii_diagram"):
                    md.append("### Architecture Diagram\n")
                    md.append("```\n")
                    md.append(arch["ascii_diagram"])
                    md.append("\n```\n")
                if arch.get("components"):
                    md.append("### Components\n")
                    for component in arch["components"]:
                        md.append(f"- **{component.get('name', 'Unknown')}**: {component.get('responsibility', 'N/A')}\n")
                        if component.get("interactions"):
                            md.append(f"  - Interactions: {component['interactions']}\n")
                if arch.get("data_flow"):
                    md.append(f"### Data Flow\n\n{arch['data_flow']}\n")
            
            return "\n".join(md)
        except Exception as e:
            return f"Error formatting documentation: {str(e)}"
