def solve_part1(puzzle: list[str]) -> None:
    """
    Print the solution of the part 1 of the day 1 puzzle
    given a list of puzzle input lines.
    """
    def line_sum(line):
        digits = [c for c in line if c.isdigit()]
        return int(digits[0] + digits[-1])
    
    print(sum(line_sum(line) for line in puzzle))

def solve_part2(puzzle: list[str]) -> None:
    """
    Print the solution of the part 2 of the day 1 puzzle
    given a list of puzzle input lines.
    """
    pass
