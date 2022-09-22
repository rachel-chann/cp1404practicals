"""
CP1404 Prac 2
Score Menu
"""

MENU = "(G)Get Score\n(R)Print Result\n(S)Print Stars\n(Q)uit"
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    """Run the score menu program."""
    score = 0
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'R':
            print(determine_score(score))
        elif choice == 'S':
            print_stars(score)
        else:
            print('Invalid choice.')
        print(MENU)
        choice = input("Choice: ").upper()
    print('Bye!')


def get_valid_score():
    """Get a valid score from user input."""
    score = float(input('Score: '))
    while score < MIN_SCORE or score > MAX_SCORE:
        print('Invalid score.')
        score = int(input('Score: '))
    return score


def determine_score(score):
    """Determine score status."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    """Print as many stars as the score."""
    print('*' * int(score))


main()
