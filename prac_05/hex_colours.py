"""
CP1404/CP5632 Practical
Hexadecimal colour codes in a dictionary
"""

NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Baby Blue": "#89cff0", "Cadet Grey": "	#91a3b0", "Daffodil": "#ffff31",
                "Earth Yellow": "#e1a95f", "Fawn": "#e5aa70", "GO Green": "#00ab66", "Han Blue": "#446ccf",
                "Iceberg": "#71a6d2", "Jade": "#00a86b"}

print(NAME_TO_CODE)

for name in NAME_TO_CODE:
    print(f"{name:13} is {NAME_TO_CODE[name]}")

color_name = input("Enter a color name: ").title()
while color_name != "":
    try:
        print(f"The color code for {color_name} is {NAME_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter a color name: ").title()
