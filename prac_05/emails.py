"""
CP1404/CP5632 Practical
Emails
Estimate: 40 minutes
Actual:   38 minutes
"""


def main():
    """Create name_to_email dictionary."""
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if name_confirmation != "Y" and name_confirmation != "":
            name = input("Name: ")
        name_to_email[name] = email
        email = input("Email: ")

    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def get_name(email):
    """Get name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
