import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    char_pool = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation

    if length < 1:
        print("Password length should be at least 1.")
        return ""

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def password_generator():
    try:
        length = int(input("Enter the desired password length: "))

        if length < 1:
            print("Password length must be greater than 0.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)

        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number for password length.")

if __name__ == "__main__":
    password_generator()
