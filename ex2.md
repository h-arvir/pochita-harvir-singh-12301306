the user: Create a function that validates email addresses

the genreated code :
import re
from typing import Optional


def validate_email(email: str) -> Optional[bool]:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        Optional[bool]: True if the email is valid, False if invalid,
                         None if the input is not a string.
    """
    if not isinstance(email, str):
        return None

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))


if __name__ == '__main__':
    # Example Usage
    email1 = "test@example.com"
    email2 = "invalid-email"
    email3 = 123

    print(f"'{email1}' is valid: {validate_email(email1)}")
    print(f"'{email2}' is valid: {validate_email(email2)}")
    print(f"'{email3}' is valid: {validate_email(email3)}")


the genrated tests:
import pytest
import re
from typing import Optional


def validate_email(email: str) -> Optional[bool]:
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        Optional[bool]: True if the email is valid, False if invalid,
                         None if the input is not a string.
    """
    if not isinstance(email, str):
        return None

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))


class TestValidateEmail:
    """
    Test suite for the validate_email function.
    """

    def test_validate_email_valid_normal(self):
        """Test with a standard valid email address."""
        assert validate_email("test@example.com") is True

    def test_validate_email_valid_with_subdomain(self):
        """Test with a valid email address containing a subdomain."""
        assert validate_email("test@sub.example.com") is True

    def test_validate_email_valid_with_numbers(self):
        """Test with a valid email address containing numbers."""
        assert validate_email("test123@example.com") is True

    def test_validate_email_valid_with_special_chars(self):
        """Test with a valid email address containing special characters."""
        assert validate_email("test.user+alias@example.com") is True

    def test_validate_email_invalid_no_at(self):
        """Test with an invalid email address missing the '@' symbol."""
        assert validate_email("testexample.com") is False

    def test_validate_email_invalid_no_domain(self):
        """Test with an invalid email address missing the domain part."""
        assert validate_email("test@.com") is False

    def test_validate_email_invalid_no_tld(self):
        """Test with an invalid email address missing the top-level domain (TLD)."""
        assert validate_email("test@example") is False

    def test_validate_email_invalid_empty_string(self):
        """Test with an empty string as input."""
        assert validate_email("") is False

    def test_validate_email_invalid_only_at_symbol(self):
        """Test with only the '@' symbol as input."""
        assert validate_email("@") is False

    def test_validate_email_invalid_starting_with_dot(self):
        """Test with an email address that starts with a dot."""
        assert validate_email(".test@example.com") is False

    def test_validate_email_invalid_ending_with_dot(self):
        """Test with an email address that ends with a dot before the @ symbol."""
        assert validate_email("test.@example.com") is False

    def test_validate_email_invalid_domain_starting_with_hyphen(self):
        """Test with an email address with a domain starting with a hyphen."""
        assert validate_email("test@-example.com") is False

    def test_validate_email_invalid_domain_ending_with_hyphen(self):
        """Test with an email address with a domain ending with a hyphen."""
        assert validate_email("test@example-.com") is False

    def test_validate_email_none_input(self):
        """Test with None as input."""
        assert validate_email(None) is None

    def test_validate_email_integer_input(self):
        """Test with an integer as input."""
        assert validate_email(123) is None

    def test_validate_email_float_input(self):
        """Test with a float as input."""
        assert validate_email(123.45) is None

    def test_validate_email_list_input(self):
        """Test with a list as input."""
        assert validate_email(["test@example.com"]) is None

the test results:
total tests: 17
passed : 13
failed : 4
test details :
test_validate_email_valid_normal
passed
✓
test_validate_email_valid_with_subdomain
passed
✓
test_validate_email_valid_with_numbers
passed
✓
test_validate_email_valid_with_special_chars
passed
✓
test_validate_email_invalid_no_at
passed
✓
test_validate_email_invalid_no_domain
passed
✓
test_validate_email_invalid_no_tld
passed
✓
test_validate_email_invalid_empty_string
passed
✓
test_validate_email_invalid_only_at_symbol
passed
✗
test_validate_email_invalid_starting_with_dot
failed
✗
test_validate_email_invalid_ending_with_dot
failed
✗
test_validate_email_invalid_domain_starting_with_hyphen
failed
✗
test_validate_email_invalid_domain_ending_with_hyphen
failed
✓
test_validate_email_none_input
passed
✓
test_validate_email_integer_input
passed
✓
test_validate_email_float_input
passed
✓
test_validate_email_list_input
passed
✗
test_validate_email_invalid_starting_with_dot
failed
✗
test_validate_email_invalid_ending_with_dot
failed
✗
test_validate_email_invalid_domain_starting_with_hyphen
failed

OUTPUT :
============================= test session starts =============================
platform win32 -- Python 3.13.7, pytest-7.4.3, pluggy-1.6.0 -- C:\Users\Harvir\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Harvir\Desktop\Project\pochita\backend
plugins: anyio-3.7.1, langsmith-0.4.38
collecting ... collected 17 items

tmpalj9pwz2.py::TestValidateEmail::test_validate_email_valid_normal PASSED [  5%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_valid_with_subdomain PASSED [ 11%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_valid_with_numbers PASSED [ 17%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_valid_with_special_chars PASSED [ 23%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_no_at PASSED [ 29%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_no_domain PASSED [ 35%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_no_tld PASSED [ 41%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_empty_string PASSED [ 47%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_only_at_symbol PASSED [ 52%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_starting_with_dot FAILED [ 58%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_ending_with_dot FAILED [ 64%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_domain_starting_with_hyphen FAILED [ 70%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_domain_ending_with_hyphen FAILED [ 76%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_none_input PASSED [ 82%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_integer_input PASSED [ 88%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_float_input PASSED [ 94%]
tmpalj9pwz2.py::TestValidateEmail::test_validate_email_list_input PASSED [100%]

================================== FAILURES ===================================
_______ TestValidateEmail.test_validate_email_invalid_starting_with_dot _______

self = <tmpalj9pwz2.TestValidateEmail object at 0x000001B676316120>

    def test_validate_email_invalid_starting_with_dot(self):
        """Test with an email address that starts with a dot."""
>       assert validate_email(".test@example.com") is False
E       AssertionError: assert True is False
E        +  where True = validate_email('.test@example.com')

tmpalj9pwz2.py:99: AssertionError
________ TestValidateEmail.test_validate_email_invalid_ending_with_dot ________

self = <tmpalj9pwz2.TestValidateEmail object at 0x000001B676316300>

    def test_validate_email_invalid_ending_with_dot(self):
        """Test with an email address that ends with a dot before the @ symbol."""
>       assert validate_email("test.@example.com") is False
E       AssertionError: assert True is False
E        +  where True = validate_email('test.@example.com')

tmpalj9pwz2.py:103: AssertionError
__ TestValidateEmail.test_validate_email_invalid_domain_starting_with_hyphen __

self = <tmpalj9pwz2.TestValidateEmail object at 0x000001B676313150>

    def test_validate_email_invalid_domain_starting_with_hyphen(self):
        """Test with an email address with a domain starting with a hyphen."""
>       assert validate_email("test@-example.com") is False
E       AssertionError: assert True is False
E        +  where True = validate_email('test@-example.com')

tmpalj9pwz2.py:107: AssertionError
___ TestValidateEmail.test_validate_email_invalid_domain_ending_with_hyphen ___

self = <tmpalj9pwz2.TestValidateEmail object at 0x000001B6763134D0>

    def test_validate_email_invalid_domain_ending_with_hyphen(self):
        """Test with an email address with a domain ending with a hyphen."""
>       assert validate_email("test@example-.com") is False
E       AssertionError: assert True is False
E        +  where True = validate_email('test@example-.com')

tmpalj9pwz2.py:111: AssertionError
=========================== short test summary info ===========================
FAILED tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_starting_with_dot
FAILED tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_ending_with_dot
FAILED tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_domain_starting_with_hyphen
FAILED tmpalj9pwz2.py::TestValidateEmail::test_validate_email_invalid_domain_ending_with_hyphen
======================== 4 failed, 13 passed in 0.25s =========================