def check_password_strength(password):
    """Check the strength of a password and provide feedback."""
    # Define a list of weak passwords
    weak_passwords = ['password', '123456', 'qwerty', 'letmein', 'admin']

    # Check if the password is in the list of weak passwords
    if password in weak_passwords:
        print("Your password is weak. Do you want to get hacked?")
    else:
        # Check the password strength based on certain criteria
        is_strong = True

        if len(password) < 8:
            is_strong = False
        elif password.isnumeric():
            is_strong = False
        elif password.isalpha():
            is_strong = False
        elif password.islower():
            is_strong = False
        elif password.isupper():
            is_strontg = False

        # Provide feedback based on password strength
        if is_strong:
            print("Congratulations! Your password is strong.")
        else:
            print("Your password is weak. Do you want to get hacked?")


# Prompt the user to enter a password
password = input("Enter your password: ")

# Check the strength of the password
check_password_strength(password)