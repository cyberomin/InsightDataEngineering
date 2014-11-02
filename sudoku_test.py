import unittest
import os
from sudoku import Sudoku


class SudokuTest(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku()
        self.sudoku_puzzle = self.sudoku.parse_csv("puzzle.csv")
        self.matrix = self.sudoku.group(self.sudoku_puzzle, 9)
        self.location = (0, 0)
    """
    def tearDown(self):
        dir = os.curdir
        file_sys = os.listdir(dir)
        filename = [f for f in file_sys if f == "solution.csv"]
        if len(filename) >= 1: os.remove(filename[0])
    """

    def test_puzzle_has_eighty_one_items(self):
        self.assertEquals(len(self.sudoku_puzzle), 81)

    def test_solve_puzzle(self):
        answer = self.sudoku.solve(self.matrix)
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

    def test_puzzle_elements_at_a_position(self):
        col_elements = self.sudoku.get_col(self.matrix, self.location)
        row_elements = self.sudoku.get_row(self.matrix, self.location)
        block_elements = self.sudoku.get_block(self.matrix, self.location)

        self.assertEquals(len(col_elements), 9)
        self.assertEquals(len(row_elements), 9)
        self.assertEquals(len(block_elements), 9)

    def test_puzzle_elements_at_row_position_are_valid(self):
        row_elements = self.sudoku.get_row(self.matrix, self.location)
        self.assertEquals(row_elements, [0,3,5,2,9,0,8,6,4])

    def test_puzzle_elements_at_col_position_are_valid(self):
        col_elements = self.sudoku.get_col(self.matrix, self.location)
        self.assertEquals(col_elements, [0,0,7,2,0,0,4,3,8])

    def test_puzzle_elements_at_block_position_are_valid(self):
        block_elements = self.sudoku.get_block(self.matrix, self.location)
        self.assertEquals(block_elements, [0, 3, 5, 0, 8, 2, 7, 6, 4])

    def test_puzzle_file_is_not_already_solved(self):
        pos = self.sudoku.find_unsolved_location(self.matrix)
        self.assertIsInstance(pos, tuple)

    def test_unassinged_location(self):
        pos = self.sudoku.find_unsolved_location(self.matrix)
        self.assertEquals(pos, (0, 0))

    def test_possible_value_is_correct(self):
        value = list(self.sudoku.find_possible_values(self.matrix, self.location))
        self.assertEquals(value[0], 1)

    def test_value_is_legal(self):
        self.assertTrue(self.sudoku.is_legal(1, self.matrix, self.location))


def main():
    unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)
    unittest.main()

if __name__ == "__main__":
    main()
