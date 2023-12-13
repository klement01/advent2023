"""
Common functions used by multiple solutions.
"""

import argparse
import pathlib

import day01.solvers
import day02.solvers

def get_lines_from_path(path: pathlib.Path) -> list[str]:
    """Return a list with the contents of all lines of the file in path."""
    with open(path, encoding="utf-8") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def __main() -> None:
    """Print the solution to the selected puzzle input and day."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog="AOC2023",
        description="Solves an Advent of Code 2023 puzzle",
    )
    parser.add_argument(
        "day",
        type=int,
        help="Day of the puzzle to be solved"
    )
    parser.add_argument(
        "part",
        type=int,
        help="Part of the puzzle to be solved"
    )
    parser.add_argument(
        "puzzle",
        type=pathlib.Path,
        help="Path to puzzle input",
    )
    args = parser.parse_args()

    # Get file contents and solver for the day
    lines = get_lines_from_path(args.puzzle)

    day = args.day
    part = args.part

    solvers = {
        1: {1: day01.solvers.solve_part1, 2: day01.solvers.solve_part2},
        2: {1: day02.solvers.solve_part1, 2: day02.solvers.solve_part2}
    }
    try:
        solver = solvers[args.day][args.part]
    except KeyError as exc:
        raise ValueError(f"Day {day}, part {part} not implemented") from exc

    # Print the solution
    solver(lines)

if __name__ == "__main__":
    __main()
else:
    raise ImportError("File shouldn't be imported.")
