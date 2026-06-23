import random
import string

class PasswordValidationError(Exception):

    pass

def generate_password(length=12):
    """Generates a secure, random password with letters, digits, and symbols."""
    if length < 8:
        print("Warning: Password length should be at least 8 characters for security.")
        length = 8

    all_characters = string.ascii_letters + string.digits + string.punctuation


    password_list = [random.choice(all_characters) for _ in range(length)]


    random.shuffle(password_list)
    password = "".join(password_list)

    return password



def validate_password(password):
    """Validates a password against safety rules and raises custom exceptions if they fail."""

    if len(password) < 8:
        raise PasswordValidationError("Password must be at least 8 characters long.")


    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        raise PasswordValidationError("Password must contain at least one uppercase letter (A-Z).")


    has_lower = any(char.islower() for char in password)
    if not has_lower:
        raise PasswordValidationError("Password must contain at least one lowercase letter (a-z).")


    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        raise PasswordValidationError("Password must contain at least one number (0-9).")


    has_special = any(char in string.punctuation for char in password)
    if not has_special:
        raise PasswordValidationError("Password must contain at least one special character (e.g., !, @, #, $, %).")

    return True



def main():
    while True:
        print("\n=== PASSWORD TOOLBOX ===")
        print("1. Generate a Strong Password")
        print("2. Validate a Password")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                length = int(input("Enter desired password length (default 12): ") or 12)
                generated_pass = generate_password(length)
                print(f"\nGenerated Secure Password: {generated_pass}")
            except ValueError:
                print("Invalid input! Please enter a valid integer number for length.")

        elif choice == "2":
            user_pass = input("Enter a password to test: ").strip()

            try:

                validate_password(user_pass)
                print(" Excellent! Your password meets all security strength rules.")
            except PasswordValidationError as error:

                print(f"Weak Password Alert: {error}")

        elif choice == "3":
            print("Exiting tool. Stay secure!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


main()
