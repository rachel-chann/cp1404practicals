"""
CP1404/CP5632 Practical
Guitars
Estimate: 20 minutes
Actual:   16 minutes
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f'{self.name} ({self.year}) : ${self.cost}'

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
