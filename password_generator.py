"""
This module provides a simple password generator that creates random passwords
containing letters, digits, and special characters.

Functions:
    generate_password(length=12):
        Generates a random password of specified length (minimum 6 characters).
        The password includes uppercase and lowercase letters, digits, and punctuation.

Usage:
    Run the script directly to use the command-line interface for generating a password.
    The user is prompted to enter the desired password length.
    If the input is invalid or less than 6, an error message is displayed.
"""
import string
import random

"""
Generates a random password containing uppercase and lowercase letters, digits, and special characters.
Args:
    length (int, optional): The length of the password to generate. Must be at least 6. Defaults to 12.
Returns:
    str: The randomly generated password.
Raises:
    ValueError: If the specified length is less than 6.
"""
def generate_password(length=12):

    if length < 6:
        raise ValueError("The minimum password length must be 6 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

if __name__ == "__main__":
    print("Generador de Contraseñas")
    try:
        length = int(input("Enter the password length (minimum 6): "))
        password = generate_password(length)
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")