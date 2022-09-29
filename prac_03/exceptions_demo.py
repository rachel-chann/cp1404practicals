"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: when the input value is not an integer
2. When will a ZeroDivisionError occur?
Ans: when the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: yes, please see the changes made below
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero. Please input again.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
