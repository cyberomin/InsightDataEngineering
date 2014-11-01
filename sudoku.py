from __future__ import division
import sys
import string
import csv


class Sudoku:

    def __init__(self, file):
        """Initialize the puzzle to solve"""
        self.file = file

    def parse_csv(self, csv_file):
        """Parse CSV gotten from the constructor and generates
        a string of numbers."""
        parsed_result = ""
        with open(csv_file, 'r') as f:
            lines = csv.reader(f)
            data = [numbers for line in lines for numbers in line]
        for x in data:
            parsed_result += x
        return parsed_result

    def solved_csv(self, result):
        """Writes the result of the puzzle in a CSV file."""
        data = []
        x = 0
        solved_file = "solution.csv"
        result = str(result)
        total = len(result) // 9
        for i in range(total):
            data.append(list(result[x:x + 9]))
            x += 9

        with open(solved_file, 'w') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerows(data)

        return solved_file

    def same_row(self, i, j):
        """Checks to see if the rows are the same"""
        return i/9 == j/9

    def same_col(self, i, j):
        """Checks to see if the column are the same"""
        return (i-j) % 9 == 0

    def same_block(self, i, j):
        return i/27 == j/27 and i % 9/3 == j % 9/3

    def solve(self, puzzle):
        """Solves the puzzle and returns a solution as CSV"""
        i = puzzle.find('0')
        if i == -1:
            self.solved_csv(puzzle)
            sys.exit(puzzle)
        excluded_numbers = set()
        for j in range(81):
            if self.same_row(i, j) \
                    or self.same_col(i, j) \
                    or self.same_block(i, j):
                excluded_numbers.add(puzzle[j])

        for m in string.digits[1:]:
            if m not in excluded_numbers:
                self.solve(puzzle[:i] + m + puzzle[i+1:])

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        sudoku = Sudoku(sys.argv[1])
        puzzle = sudoku.parse_csv(sudoku.file)
        sudoku.solve(puzzle)
        print "Solved. The result is in solution.csv"
    else:
        print 'Usage: python sudoku.py puzzle.csv'
        print 'The puzzle.csv is a 9 x 9 file where 0 represents ' \
              'unsolved location or blanks.'
