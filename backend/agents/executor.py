"""
Code Executor - Custom sandbox wrapper around subprocess
Safe code execution with error handling and output parsing
"""

import subprocess
import os
import tempfile
from typing import Dict, Tuple


class CodeExecutor:
    """Executes Python code in a sandboxed environment"""
    
    TIMEOUT = 10  # seconds
    
    @staticmethod
    def execute(code: str, test_mode: bool = False) -> Dict:
        """
        Execute Python code safely
        
        Args:
            code: Python code to execute
            test_mode: If True, run as pytest
        
        Returns:
            Dict with status, output, and errors
        """
        try:
            with tempfile.NamedTemporaryFile(
                mode='w',
                suffix='.py',
                delete=False,
                dir=os.getcwd()
            ) as f:
                f.write(code)
                temp_file = f.name
            
            try:
                if test_mode:
                    # Run as pytest
                    result = subprocess.run(
                        ["python", "-m", "pytest", temp_file, "-v"],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.TIMEOUT
                    )
                else:
                    # Run as regular script
                    result = subprocess.run(
                        ["python", temp_file],
                        capture_output=True,
                        text=True,
                        timeout=CodeExecutor.TIMEOUT
                    )
                
                return {
                    "status": "success" if result.returncode == 0 else "failed",
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "returncode": result.returncode
                }
            
            finally:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
        
        except subprocess.TimeoutExpired:
            return {
                "status": "timeout",
                "stdout": "",
                "stderr": f"Execution timed out after {CodeExecutor.TIMEOUT}s",
                "returncode": -1
            }
        except Exception as e:
            return {
                "status": "error",
                "stdout": "",
                "stderr": str(e),
                "returncode": -1
            }