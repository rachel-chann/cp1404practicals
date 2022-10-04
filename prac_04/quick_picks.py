"""
CP1404/CP5632 Practical
Quick Picks
"""

from random import randint

NUMBERS_PER_LINE = 6
MIN_VALUE = 1
MAX_VALUE = 45

number_of_quick_picks = int(input('How many quick picks? '))
for i in range(number_of_quick_picks):
    quick_picks = []
    for j in range(NUMBERS_PER_LINE):
        number = randint(MIN_VALUE, MAX_VALUE)
        while number in quick_picks:
            number = randint(MIN_VALUE, MAX_VALUE)
        quick_picks.append(number)
    quick_picks.sort()
    print(' '.join(f'{number:2}' for number in quick_picks))
