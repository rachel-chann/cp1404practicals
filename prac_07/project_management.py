"""
CP1404/CP5632 Practical
Project Management Program
Estimate: 200 minutes
Actual:
"""
MENU = '- (L)oad projects\n- (S)ave projects\n- (D)isplay projects' \
       '\n- (F)ilter projects by date\n- (A)dd new project\n- (U)date project\n- (Q)uit'
FILENAME = 'projects.txt'


def main():
    """Project management program."""
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input('File to load: ')
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input('File to save: ')
            save_projects(projects, filename)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print('Invalid menu choice')
        print(MENU)
        choice = input('>>> ').upper()
    save_projects(projects, FILENAME)
    print('Thank you for using custom-built project management software.')


def load_projects(filename):
    """Load projects from tab-delimited text file."""
    pass


def display_projects(projects):
    """Display in two groups: incomplete projects; complete projects, both sorted by priority."""
    pass


def add_project(projects):
    """Add new project object to the list."""
    pass


def filter_projects(projects):
    """Filter and sort projects by the date."""
    pass


def update_project(projects):
    """Get project choice and update based on user input values."""
    pass


def save_projects(projects, filename):
    """Save projects to tab-delimited text file."""
    pass


main()
