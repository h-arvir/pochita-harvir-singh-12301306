the user: Create a function that validates email addresses

the Generated code :
import re
from typing import Optional


def validate_email(email: str) -> Optional[bool]:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        Optional[bool]: True if the email is valid, False if invalid,
                         and None if the input is not a string.
    """
    if not isinstance(email, str):
        return None

    # Regular expression for validating an email address.
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check if the email matches the regex.
    if re.match(email_regex, email):
        return True
    else:
        return False

the generated tests:
import pytest
from typing import Optional
from your_module import validate_email  # Replace your_module


class TestValidateEmail:
    """
    Test suite for the validate_email function.
    """

    def test_validate_email_normal_valid(self):
        """
        Test with a normal, valid email address.
        """
        assert validate_email("test@example.com") is True

    def test_validate_email_normal_valid_with_subdomain(self):
        """
        Test with a valid email address including a subdomain.
        """
        assert validate_email("test@sub.example.com") is True

    def test_validate_email_normal_valid_with_numbers(self):
        """
        Test with a valid email address including numbers.
        """
        assert validate_email("test123@example.com") is True

    def test_validate_email_edge_empty(self):
        """
        Test with an empty email string.
        """
        assert validate_email("") is False

    def test_validate_email_edge_invalid_no_at(self):
        """
        Test with an invalid email address missing the '@' symbol.
        """
        assert validate_email("testexample.com") is False

    def test_validate_email_edge_invalid_no_domain(self):
        """
        Test with an invalid email address missing the domain.
        """
        assert validate_email("test@.com") is False

    def test_validate_email_edge_invalid_no_tld(self):
        """
        Test with an invalid email address missing the top-level domain (TLD).
        """
        assert validate_email("test@example") is False

    def test_validate_email_edge_invalid_space(self):
        """
        Test with an invalid email address containing a space.
        """
        assert validate_email("test @example.com") is False

    def test_validate_email_edge_long_tld(self):
        """
        Test with a valid email address with a longer TLD.
        """
        assert validate_email("test@example.museum") is True

    def test_validate_email_error_none(self):
        """
        Test with None as input.
        """
        assert validate_email(None) is None

    def test_validate_email_error_integer(self):
        """
        Test with an integer as input.
        """
        assert validate_email(123) is None

    def test_validate_email_error_list(self):
        """
        Test with a list as input.
        """
        assert validate_email(["test@example.com"]) is None

    def test_validate_email_normal_valid_with_plus(self):
        """
        Test with a valid email address including a plus sign.
        """
        assert validate_email("test+alias@example.com") is True

    def test_validate_email_normal_valid_with_underscore(self):
        """
        Test with a valid email address including an underscore.
        """
        assert validate_email("test_alias@example.com") is True

    def test_validate_email_normal_valid_with_hyphen(self):
        """
        Test with a valid email address including a hyphen.
        """
        assert validate_email("test-alias@example.com") is True

test results :
total test : 1
passed : 0
failed : 0
output :
============================= test session starts =============================
platform win32 -- Python 3.13.7, pytest-7.4.3, pluggy-1.6.0 -- C:\Users\Harvir\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Harvir\Desktop\Project\pochita\backend
plugins: anyio-3.7.1, langsmith-0.4.38
collecting ... collected 0 items / 1 error

=================================== ERRORS ====================================
_______________________ ERROR collecting tmp5iwo7ktp.py _______________________
ImportError while importing test module 'C:\Users\Harvir\Desktop\Project\pochita\backend\tmp5iwo7ktp.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\..\..\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tmp5iwo7ktp.py:30: in <module>
    from your_module import validate_email  # Replace your_module
E   ModuleNotFoundError: No module named 'your_module'
=========================== short test summary info ===========================
ERROR tmp5iwo7ktp.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.24s ===============================