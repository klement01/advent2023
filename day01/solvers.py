"""
Day 1: <https://adventofcode.com/2023/day/1>
"""


def line_sum(line):
    """Return the sum for a single line."""
    digits = [c for c in line if c.isdigit()]
    return int(digits[0] + digits[-1])


def solve_part1(puzzle: list[str]) -> None:
    """
    Print the solution of the part 1 of the day 1 puzzle
    given a list of puzzle input lines.
    """
    print(sum(line_sum(line) for line in puzzle))


def solve_part2(puzzle: list[str]) -> None:
    """
    Print the solution of the part 2 of the day 1 puzzle
    given a list of puzzle input lines.
    """

    def line_replace(line):
        pairs = (
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
        )

        # Replace the first occurence of a digit until are are replaced
        while True:
            hits = [
                (spot, name, digit)
                for name, digit in pairs
                if (spot := line.find(name)) != -1
            ]
            if len(hits) == 0:
                break
            _, name, digit = min(hits, key=lambda x: x[0])
            # Doesn't replace the last letter to allow the replacements
            # eighthree -> 83, sevenine -> 79
            line = line.replace(name[:-1], digit, 1)

        return line

    puzzle = [line_replace(line) for line in puzzle]
    print(sum(line_sum(line) for line in puzzle))
