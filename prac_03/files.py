"""
CP1404/CP5632 - Files Program
"""

# 1
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt")
name = in_file.read()
in_file.close()
print(f'Your name is {name}')

# 3
in_file = open("numbers.txt")
numbers = in_file.readlines()
in_file.close()
result = int(numbers[0]) + int(numbers[1])
print(result)

# 4
in_file = open("numbers.txt")
numbers = in_file.readlines()
in_file.close()
result = 0
for number in numbers:
    result += int(number)
print(result)
