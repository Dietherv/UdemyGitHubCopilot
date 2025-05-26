import pytest
import string
from password_generator import generate_password

def test_generate_password_default_length():
    password = generate_password()
    assert isinstance(password, str)
    assert len(password) == 12

def test_generate_password_custom_length():
    length = 20
    password = generate_password(length)
    assert isinstance(password, str)
    assert len(password) == length

def test_generate_password_minimum_length():
    password = generate_password(6)
    assert isinstance(password, str)
    assert len(password) == 6

def test_generate_password_invalid_length():
    with pytest.raises(ValueError):
        generate_password(5)

def test_generate_password_characters():
    password = generate_password(50)
    allowed_chars = set(string.ascii_letters + string.digits + string.punctuation)
    assert all(c in allowed_chars for c in password)