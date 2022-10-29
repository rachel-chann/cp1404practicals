"""
CP1404/CP5632 Practical
Guitars
Estimate: 30 minutes
Actual:   32 minutes
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")

while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(new_guitar, 'added')
    print()
    name = input("Name: ")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print()
print('... snip ...')
print()
print("These are my guitars:")

for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
