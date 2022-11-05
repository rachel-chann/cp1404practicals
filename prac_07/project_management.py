"""
CP1404/CP5632 Practical
Project Management Program
Estimate: 200 minutes
Actual:
"""
import datetime
from prac_07.project import Project
from operator import attrgetter

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
    projects = []
    with open(filename) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strptime(parts[1], '%d/%m/%Y').date()
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]),)
            projects.append(project)
    return projects


def display_projects(projects):
    """Display in two groups: incomplete projects; complete projects, both sorted by priority."""
    print('Incomplete projects: ')
    incomplete_projects = [project for project in projects if not project.is_completed()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(' ', project)
    print('Completed projects: ')
    complete_projects = [project for project in projects if project.is_completed()]
    complete_projects.sort()
    for project in complete_projects:
        print(' ', project)


def add_project(projects):
    """Add new project object to the list."""
    print("Let's add a new project")
    name = input('Name: ')
    start_date = get_date('Start date (dd/mm/yy): ')
    priority = int(input('Priority: '))
    cost_estimate = float(input('Cost estimate: $'))
    percentage_complete = int(input('Percent complete: '))
    new_project = Project(name, start_date, priority, cost_estimate, percentage_complete)
    projects.append(new_project)


def filter_projects(projects):
    """Filter and sort projects by the date."""
    start_date = get_date('Show projects that start after date (dd/mm/yy): ')
    requested_projects = [project for project in projects if project.start_date >= start_date]
    requested_projects.sort(key=attrgetter('start_date'))
    for project in requested_projects:
        print(project)


def update_project(projects):
    """Get project choice and update based on user input values."""
    for i, project in enumerate(projects):
        print(i, project)
    index = int(input('Project choice: '))
    project = projects[index]
    print(project)
    try:
        percentage_complete = int(input('New Percentage: '))
        project.percentage_complete = percentage_complete
    except ValueError:
        pass
    try:
        priority = int(input('New Priority: '))
        project.priority = priority
    except ValueError:
        pass


def save_projects(projects, filename):
    """Save projects to tab-delimited text file."""
    pass


def get_date(prompt):
    """Get the date object from the input date string."""
    date = input(prompt)
    date = datetime.datetime.strptime(date, '%d/%m/%Y').date()
    return date


main()
