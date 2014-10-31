import unittest
import csv
from sudoku import Sudoku

class SudokuTest(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku("puzzle.csv")

    def test_puzzle_has_eighty_one_items(self):
        sudoku_puzzle = self.sudoku.parse_csv(self.sudoku.file)
        self.assertEquals(len(sudoku_puzzle), 81)

    def test_solution_is_csv(self):
        puzzle = self.sudoku.parse_csv(self.sudoku.file)
        result = self.sudoku.solved_csv(puzzle)
        self.assertTrue(result.endswith("csv"))

    def test_solution_has_eighty_one_items(self):
        sudoku_puzzle = self.sudoku.parse_csv("solution.csv")
        self.assertEquals(len(sudoku_puzzle), 81)


    def test_solution_is_correct(self):
        puzzle = self.sudoku.parse_csv(self.sudoku.file)
        self.sudoku.solve(puzzle)

        parsed_result = ""
        with open("solution.csv", 'r') as f:
            lines = csv.reader(f)
            data = [numbers for line in lines for numbers in line]
        for x in data:
            parsed_result += x
        self.assertFalse(0 in parsed_result)




def main():
    unittest.main()

if __name__ == "__main__":
    main()