"""
CP5632
Band class
"""
from prac_09.musician import Musician


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a band with a name and empty musician collection."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a band."""
        return f"{self.name} ({self.members})"

    def __repr__(self):
        """Return a string representation of a band, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a musician to band's members."""
        self.members.append(member)

    def play(self):
        """Return a string showing the members playing their first (or no) instrument."""
        for member in self.members:
            return Musician(member).play()

