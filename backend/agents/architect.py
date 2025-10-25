"""
Architect Agent - Analyzes requirements and designs solution architecture
Creates high-level design plans before code generation
"""

import google.generativeai as genai
import os


class ArchitectAgent:
    """Agent responsible for architectural analysis and design planning"""
    
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        
        self.prompt_template = """You are an expert software architect. Analyze the given requirement and provide a detailed architectural design.

User Requirement: {requirement}

Provide architectural guidance including:
- **Problem Analysis**: Understand what needs to be built
- **Solution Approach**: High-level design strategy
- **Key Components**: Main modules/functions needed
- **Data Structures**: Recommended data structures and types
- **Error Handling**: Key error cases to consider
- **Edge Cases**: Important edge cases and boundaries
- **Performance Considerations**: Any performance implications

Format your response clearly with sections and bullet points.
Be concise but comprehensive in your analysis."""
    
    def generate(self, requirement: str) -> str:
        """Generate architectural analysis for given requirement"""
        try:
            prompt = self.prompt_template.format(requirement=requirement)
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                )
            )
            architecture = response.text
            return self._format_architecture(architecture)
        except Exception as e:
            return f"Error generating architecture: {str(e)}"
    
    def _format_architecture(self, architecture: str) -> str:
        """Format and clean up architectural output"""
        architecture = architecture.strip()
        if not architecture:
            return "Error: No architecture generated"
        return architecture
