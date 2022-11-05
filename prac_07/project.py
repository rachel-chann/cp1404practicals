"""
CP1404/CP5632 Practical
Project Management Program
Estimate: 200 minutes
Actual:   190 minutes
"""


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, percentage_complete):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage_complete = percentage_complete

    def __repr__(self):
        """Return string representation of a Project."""
        return f'{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, ' \
               f'estimate: ${self.cost_estimate:.2f}, completion: {self.percentage_complete}%'

    def __lt__(self, other):
        """Sort the projects by priority."""
        return self.priority < other.priority

    def is_completed(self):
        """Determine if the project is completed."""
        return self.percentage_complete == 100
