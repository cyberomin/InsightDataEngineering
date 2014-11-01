import unittest
from sudoku import Sudoku
import os


class SudokuTest(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku()

    """
    def test_input_is_csv(self):
        puzzle_file = sys.argv[1]
        self.assertTrue(puzzle_file.endswith("csv"))
    """

    def test_puzzle_has_eighty_one_items(self):
        sudoku_puzzle = self.sudoku.parse_csv("puzzle.csv")
        self.assertEquals(len(sudoku_puzzle), 81)

    def test_solve_puzzle(self):
        sudoku_num = self.sudoku.parse_csv("puzzle.csv")
        matrix = self.sudoku.group(sudoku_num, 9)
        answer = self.sudoku.solve(matrix)
        self.sudoku.write_to_csv(answer)
        dir = os.curdir
        file_sys = os.listdir(dir)
        self.assertIn("solution.csv", file_sys)

    def test_solution_has_eighty_one_items(self):
        sudoku_puzzle = self.sudoku.parse_csv("solution.csv")
        self.assertEquals(len(sudoku_puzzle), 81)

    def test_solution_is_correct(self):
        solution = self.sudoku.parse_csv("solution.csv")
        matrix = self.sudoku.group(solution, 9)
        for line in matrix:
            self.assertEquals(sorted(line), range(1, 10))

    def test_solution_is_csv(self):
        puzzle_file = "solution.csv"
        self.assertTrue(puzzle_file.endswith("csv"))

    def test_elements_at_a_position(self):
        sudoku_puzzle = self.sudoku.parse_csv("puzzle.csv")
        matrix = self.sudoku.group(sudoku_puzzle, 9)
        location = (0, 0)

        col_elements = self.sudoku.get_col(matrix, location)
        row_elements = self.sudoku.get_row(matrix, location)
        block_elements = self.sudoku.get_block(matrix, location)

        self.assertEquals(len(col_elements), 9)
        self.assertEquals(len(row_elements), 9)
        self.assertEquals(len(block_elements), 9)


def main():
    unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)
    unittest.main()

if __name__ == "__main__":
    main()
