"""
CP1404/CP5632 Practical
More Guitars
"""
import csv
from prac_06.guitar import Guitar

FILENAME = 'guitars.csv'

in_file = open(FILENAME, 'r', newline='')
reader = csv.reader(in_file)
guitars = []
for row in reader:
    row[1] = int(row[1])
    row[2] = float(row[2])
    guitar = Guitar(row[0], row[1], row[2])
    guitars.append(guitar)
in_file.close()
guitars.sort()
for guitar in guitars:
    print(guitar)

print()
name = input("Name: ")
year = int(input("Year: "))
cost = float(input("Cost: $"))
new_guitar = Guitar(name, year, cost)
guitars.append(new_guitar)
new_guitar_details = [name, year, cost]
out_file = open(FILENAME, 'a', newline='')
writer = csv.writer(out_file)
writer.writerow(new_guitar_details)
out_file.close()
print(new_guitar, 'added')
