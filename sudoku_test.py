import unittest
import os
from sudoku import Sudoku


class SudokuTest(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku()
        self.sudoku_puzzle = self.sudoku.parse_csv("puzzle.csv")

    def test_puzzle_has_eighty_one_items(self):
        self.assertEquals(len(self.sudoku_puzzle), 81)

    def test_solve_puzzle(self):
        matrix = self.sudoku.group(self.sudoku_puzzle, 9)
        answer = self.sudoku.solve(matrix)
        self.sudoku.write_to_csv(answer)
        dir = os.curdir
        file_sys = os.listdir(dir)
        self.assertIn("solution.csv", file_sys)

    def test_solution_has_eighty_one_items(self):
        solution = self.sudoku.parse_csv("solution.csv")
        self.assertEquals(len(solution), 81)

    def test_solution_is_correct(self):
        solution = self.sudoku.parse_csv("solution.csv")
        matrix = self.sudoku.group(solution, 9)
        for line in matrix:
            self.assertEquals(sorted(line), range(1, 10))

    def test_solution_is_csv(self):
        puzzle_file = "solution.csv"
        self.assertTrue(puzzle_file.endswith("csv"))

    def test_elements_at_a_position(self):
        matrix = self.sudoku.group(self.sudoku_puzzle, 9)
        location = (0, 0)

        col_elements = self.sudoku.get_col(matrix, location)
        row_elements = self.sudoku.get_row(matrix, location)
        block_elements = self.sudoku.get_block(matrix, location)

        self.assertEquals(len(col_elements), 9)
        self.assertEquals(len(row_elements), 9)
        self.assertEquals(len(block_elements), 9)

    def test_input_file_is_not_already_solved(self):
        matrix = self.sudoku.group(self.sudoku_puzzle, 9)
        pos = self.sudoku.find_unsolved_location(matrix)
        self.assertIsInstance(pos, tuple)

    def test_possible_value_is_correct(self):
        matrix = self.sudoku.group(self.sudoku_puzzle, 9)
        pos = (0, 0)
        value = list(self.sudoku.find_possible_values(matrix, pos))
        self.assertEquals(value[0], 1)

    def test_value_is_legal(self):
        matrix = self.sudoku.group(self.sudoku_puzzle, 9)
        pos = (0, 0)
        self.assertTrue(self.sudoku.is_legal(1, matrix, pos))


def main():
    unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)
    unittest.main()

if __name__ == "__main__":
    main()
