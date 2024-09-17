# Sudoku Solver

This Python program solves a 9x9 Sudoku puzzle using a backtracking algorithm. The puzzle is represented by a 2D list where empty spaces are marked as `-1`.

## How it works

1. The function `find_next_empty` locates the next empty spot (represented by `-1`) in the puzzle.
2. The function `is_valid` checks if a number can be placed in a specific row, column, and 3x3 sub-grid.
3. The function `solve_sudoku` applies the backtracking algorithm, making guesses and checking if the puzzle can be solved by filling all the empty spaces.