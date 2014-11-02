##### Insight Data Engineering Challenge!
###### Sudoku puzzle Solver

This is a solution to the Insight Data Engineering Challenge. It is a sudoku puzzle solver implemented in Python.
It is requires Python 2.7 to run efficiently.

It can be ran from a unix terminal. It accepts a CSV file for the puzzle as an input and it outputs a CSV too for its solution.
The CSV is named solution.csv

```shell
$ python sudoku.py puzzle3.csv pattern=6 #Use this if input file is a 6 x 6 puzzle
$ python sudoku.py puzzle2.csv pattern=4 #Use this if input file is a 4 x 4 puzzle
$ python sudoku.py puzzle.csv pattern=9 #Use this if input file is a 9 x 9 puzzle
$ python sudoku.py puzzle.csv #Use this if input file is a 9 x 9 puzzle
``` 
The pattern parameter is optional. Running the code without this will assume the puzzle is a 9 x 9 matrix.
The soulution.csv is typically stored in the project root.

