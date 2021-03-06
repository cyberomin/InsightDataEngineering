"""Sudoko Solver
Description: The Sudoku solver Accepts a sudoku puzzle in CSV format and
recursively adds a valid input to the unsolved location
until the puzzle has reached a valid solution.
It returns a CSV as its result.
"""
from __future__ import division
import csv
from math import sqrt


class Sudoku(object):
    """A sudoku solver that uses a recursive strategy"""

    def __init__(self, pattern=None):
        """Initialize the puzzle to solve"""
        if pattern:
            self.rows = pattern
            self.cols = pattern
        else:
            self.rows = 9
            self.cols = 9

    def parse_csv(self, csv_file):
        """Parse CSV gotten from the constructor and generates
        a string of numbers."""
        try:
            with open(csv_file, 'r') as file_to_read:
                csv_reader = csv.reader(file_to_read)
                try:
                    data = [numbers for line in csv_reader for numbers in line]
                except csv.Error as error:
                    sys.exit('file %s, line %d: %s' %
                             (csv_file, csv_reader.line_num, error))
        except IOError:
            sys.exit("File does not exist")

        parsed_result = "".join(data)
        if len(parsed_result) != self.cols * self.rows:
            sys.exit("Wrong type parameter entered and or wrong puzzle file. ")
        return parsed_result

    @staticmethod
    def write_to_csv(result):
        """Writes the result of the puzzle in a CSV file."""
        if isinstance(result, list):
            solved_file = "solution.csv"
            with open(solved_file, 'w') as file_to_process:
                writer = csv.writer(file_to_process, delimiter=',')
                writer.writerows(result)
        else:
            raise Exception("Please supply a list")

    @staticmethod
    def group(puzzle, num):
        """Arrange the puzzle as an n x n matrix"""
        result = []
        grid = [puzzle[i:i+num] for i in range(0, len(puzzle), num)]
        for line in grid:
            result.append([int(y) for y in line])
        return result

    def find_unsolved_location(self, grid):
        """Find unsolved location across the matirx"""
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 0:
                    return (row, col)

    @staticmethod
    def get_row(grid, pos):
        """Get the row element for the current position
        1 2 3 4 5 6 7 8 9
        """
        row = pos[0]
        return [x for x in grid[row]]

    def get_col(self, grid, pos):
        """Get the column element for the current position
        1
        2
        3
        4
        5
        6
        7
        8
        9
        """
        row, col = pos
        return [grid[row][col] for row in range(self.rows)]

    def get_block(self, grid, pos):
        """Get the block for the current position
        1 2 3
        4 5 6
        7 8 9
        """
        row, cow = pos
        rows = int(sqrt(self.rows))
        cols = int(sqrt(self.cols))
        peer_row = rows * (row // rows)
        peer_col = cols * (cow // cols)
        return [grid[peer_row + r][peer_col + c] for r in range(rows)
                for c in range(cols)]

    def find_possible_values(self, grid, pos):
        """Find a possible value for the unsolved location"""
        return set(range(1, self.rows + 1)) - \
            set(self.get_row(grid, pos)) - \
            set(self.get_col(grid, pos)) - \
            set(self.get_block(grid, pos))

    def solve(self, grid):
        """Solve sudoku puzzle"""
        pos = self.find_unsolved_location(grid)
        solution = ""
        if not pos:
            return grid
        row, col = pos
        for value in self.find_possible_values(grid, pos):
            # Number hasn't been used across row and column
            if self.is_legal(value, grid, pos):
                grid[row][col] = int(value)
            solution = self.solve(grid)
        if solution:
            return solution
        grid[row][col] = 0  # could not find a solution, fix in a zero there.

    def is_legal(self, value, grid, pos):
        """Check if the value can fit into the current position"""
        return value not in self.get_row(grid, pos) and \
            self.get_col(grid, pos) and \
            self.get_block(grid, pos)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        sudoku = Sudoku()
        sudoku_num = sudoku.parse_csv(sys.argv[1])
        matrix = sudoku.group(sudoku_num, 9)
        answer = sudoku.solve(matrix)
        sudoku.write_to_csv(answer)
        print "Solved. The result is in solution.csv"

    elif len(sys.argv) == 3 \
            and sys.argv[1].endswith(".csv") \
            and sys.argv[2].startswith("pattern="):
        num_format = sys.argv[2].split("=")[1]
        num_format = int(num_format)
        acceptable = (4, 6, 9)
        if num_format in acceptable:
            sudoku = Sudoku(num_format)
            sudoku_num = sudoku.parse_csv(sys.argv[1])
            matrix = sudoku.group(sudoku_num, num_format)
            answer = sudoku.solve(matrix)
            sudoku.write_to_csv(answer)
            print "Solved. The result is in solution.csv"
        else:
            print "Invalid type entered", num_format

    else:
        print 'Usage: python sudoku.py puzzle.csv'
        print 'The puzzle.csv should be a 9 x 9, 4 * 4 or a 6 x6 file ' \
              'where 0 represents unsolved location or blanks.'
