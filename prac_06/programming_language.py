"""
CP1404/CP5632 Practical
Programming Language Class
Estimate: 20 minutes
Actual:   16 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a programming language object."""
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'

    def is_dynamic(self):
        """Determine if a programming language is dynamic."""
        return self.typing == 'Dynamic'
