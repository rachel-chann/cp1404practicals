MIN_LENGTH = 6
password = input("password: ")
while len(password) < MIN_LENGTH:
    print(f"The password should be consisted of at least {MIN_LENGTH} characters.")
    password = input("password: ")
print(f'password: {len(password) * "*"}')
