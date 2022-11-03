"""
CP1404/CP5632 Practical
More Guitars
"""
import csv

from prac_06.guitar import Guitar

in_file = open('guitars.csv', 'r', newline='')
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
