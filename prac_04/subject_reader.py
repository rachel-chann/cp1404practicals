"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Generate formatted subject details from file."""
    data = get_data()
    print_subject_details(data)


def print_subject_details(data):
    """Print the formatted subject details."""
    for subject_details in data:
        print(f"{subject_details[0]} is taught by {subject_details[1]:12} and has {subject_details[2]:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


main()
