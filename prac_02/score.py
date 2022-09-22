"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    """Print score status."""
    score = float(input("Enter score: "))
    print(determine_score(score))
    random_score = randint(0, 100)
    print(determine_score(random_score))


def determine_score(score):
    """Determine score status."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
