"""
Result Parser - Parses test output and extracts pass/fail information
Custom parsing logic for pytest output and error handling
"""

import re
from typing import Dict, List, Tuple


class ResultParser:
    """Parses code execution and test results"""
    
    @staticmethod
    def parse_test_results(output: str, returncode: int) -> Dict:
        """
        Parse pytest test results from output
        
        Args:
            output: Pytest output string
            returncode: Process return code
        
        Returns:
            Dict with parsed results including pass/fail counts and details
        """
        result = {
            "status": "passed" if returncode == 0 else "failed",
            "total": 0,
            "passed": 0,
            "failed": 0,
            "errors": 0,
            "skipped": 0,
            "test_details": [],
            "summary": "",
            "raw_output": output
        }
        
        passed_count = ResultParser._extract_count(output, r"(\d+) passed")
        failed_count = ResultParser._extract_count(output, r"(\d+) failed")
        error_count = ResultParser._extract_count(output, r"(\d+) error")
        skipped_count = ResultParser._extract_count(output, r"(\d+) skipped")
        
        result["passed"] = passed_count
        result["failed"] = failed_count
        result["errors"] = error_count
        result["skipped"] = skipped_count
        result["total"] = passed_count + failed_count + error_count
        
        result["test_details"] = ResultParser._extract_test_details(output)
        result["summary"] = ResultParser._generate_summary(result)
        
        return result
    
    @staticmethod
    def parse_execution_results(stdout: str, stderr: str, returncode: int) -> Dict:
        """
        Parse regular code execution results
        
        Args:
            stdout: Standard output
            stderr: Standard error
            returncode: Process return code
        
        Returns:
            Dict with execution results
        """
        return {
            "status": "success" if returncode == 0 else "failed",
            "output": stdout,
            "error": stderr,
            "returncode": returncode,
            "has_error": returncode != 0 or bool(stderr)
        }
    
    @staticmethod
    def _extract_count(text: str, pattern: str) -> int:
        """Extract count from regex pattern"""
        match = re.search(pattern, text)
        return int(match.group(1)) if match else 0
    
    @staticmethod
    def _extract_test_details(output: str) -> List[Dict]:
        """Extract individual test results"""
        test_details = []
        
        patterns = [
            (r"(PASSED|FAILED|ERROR)\s+(.*?)(?=\n|$)", None),
            (r"(test_\w+)\s+(PASSED|FAILED|ERROR)", None),
            (r"::(test_\w+)\s+(PASSED|FAILED)", None),
        ]
        
        for match in re.finditer(r"(test_\w+)\s*(?:\[(.*?)\])?\s*(PASSED|FAILED|ERROR)", output):
            test_name = match.group(1)
            params = match.group(2) or ""
            status = match.group(3).lower()
            
            test_details.append({
                "name": test_name,
                "params": params,
                "status": status
            })
        
        if not test_details:
            if "PASSED" in output:
                test_details.append({
                    "name": "tests",
                    "params": "",
                    "status": "passed"
                })
            elif "FAILED" in output or "ERROR" in output:
                test_details.append({
                    "name": "tests",
                    "params": "",
                    "status": "failed"
                })
        
        return test_details
    
    @staticmethod
    def _generate_summary(result: Dict) -> str:
        """Generate human-readable summary"""
        if result["total"] == 0:
            return "No tests found"
        
        summary_parts = []
        if result["passed"] > 0:
            summary_parts.append(f"{result['passed']} passed")
        if result["failed"] > 0:
            summary_parts.append(f"{result['failed']} failed")
        if result["errors"] > 0:
            summary_parts.append(f"{result['errors']} errors")
        if result["skipped"] > 0:
            summary_parts.append(f"{result['skipped']} skipped")
        
        summary = ", ".join(summary_parts)
        
        if result["status"] == "passed":
            summary += " ✓"
        else:
            summary += " ✗"
        
        return summary
    
    @staticmethod
    def should_retry(result: Dict) -> bool:
        """Determine if tests should be retried"""
        return result["failed"] > 0 or result["errors"] > 0
