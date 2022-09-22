"""
CP1404 Prac 2
Password Star
"""

MIN_LENGTH = 6


def main():
    """Print asterisks as long as the input password."""
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("password: ")
    while len(password) < MIN_LENGTH:
        print(f"The password should be consisted of at least {MIN_LENGTH} characters.")
        password = input("password: ")
    return password


def print_asterisks(password):
    print(f'password: {len(password) * "*"}')


main()
