def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column
    
    return None, None

def is_valid(puzzle, guess, row, column):
    # checking if the guess exists in the given row
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    # checking if the guess exists in the given column
    column_values = [puzzle[i][column] for i in range(9)]
    if guess in column_values:
        return False
    
    # checking for the presence of our guess in the 3x3 space
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(column_start, column_start+3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    # chosing somewhere to make a guess
    row, column = find_next_empty(puzzle)

    # returning True is the board is filled
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][column] = -1

    return False

if __name__ == '__main__':
    # trying out the code
    example_board = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]

    if solve_sudoku(example_board):
        print("Solved Puzzle:-")
        for row in example_board:
            print(row)
    else: print("This can't be solved!")
