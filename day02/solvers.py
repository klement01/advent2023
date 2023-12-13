"""
Day 2: <https://adventofcode.com/2023/day/2>
"""

from functools import reduce


def parse_game(game: str) -> (int, list[dict[str:int]]):
    """
    Return the ID of the game and a list of dictionaries representing
    each set, in the form color:number of cubes.
    """
    game_id, sets = game.split(":")

    _, game_id = game_id.split(" ")
    game_id = int(game_id)

    sets = [[t.strip() for t in s.split(",")] for s in sets.split(";")]
    sets = [{color: int(n) for r in s for n, color in [r.split()]} for s in sets]

    return game_id, sets


def is_valid_set(s: dict[str:int], bag: dict[str:int]) -> bool:
    """Returns whether a set could have happened with a certain bag."""
    return all(n <= bag[color] for color, n in s.items())


def is_valid_game(game: str, bag: dict[str:int]) -> int:
    """Return 0 if the game is not valid, its ID otherwise."""
    game_id, sets = parse_game(game)
    return game_id if all(is_valid_set(s, bag) for s in sets) else 0


def game_power(game: str) -> int:
    """Return the power of the game."""
    _, sets = parse_game(game)
    colors = {color for s in sets for color, _ in s.items()}
    ns = {max(0 if color not in s else s[color] for s in sets) for color in colors}
    return reduce(lambda x, y: x * y, ns)


def solve_part1(puzzle: list[str]) -> None:
    """
    Print the solution of the part 1 of the day 2 puzzle
    given a list of puzzle input lines.
    """
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    print(sum(is_valid_game(game, bag) for game in puzzle))


def solve_part2(puzzle: list[str]) -> None:
    """
    Print the solution of the part 2 of the day 2 puzzle
    given a list of puzzle input lines.
    """
    #TODO: too low
    print(sum(game_power(game) for game in puzzle))
