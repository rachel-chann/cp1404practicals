"""
CP1404/CP5632 Practical
Game, Set, Match
Estimate: 50 minutes
Actual:   49 minutes
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Load data file and print information about Wimbledon champions."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    print_results(champion_to_count, countries)


def process_records(records):
    """Create champion dictionary and country set."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        champion_to_count[record[CHAMPION_INDEX]] = champion_to_count.get(record[CHAMPION_INDEX], 0) + 1
    return champion_to_count, countries


def print_results(champion_to_count, countries):
    """Print champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    """Extract records from file in the list of lists structure."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
