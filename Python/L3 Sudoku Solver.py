# Write a function that will solve a 9x9 Sudoku puzzle. The function will take one 
# argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

# The Sudokus tested against your function will be "easy" (i.e. determinable; there will be 
# no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]

# sudoku(puzzle)
# # Should return
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]

def solution(row, col, number, board):
    for i in range(9):
        if board[row][i] == number:
            return False
        if board[i][col] == number:
            return False
        row0 = (row // 3) *3
        col0 = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[row0+i][col0+j] == number:
                    return False
    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                is_solved = False
                for number in range(1, 10):
                    if solution(row, col, number, board):
                        board[row][col] = number
                        is_solved = solve(board)
                        if not is_solved:
                            board[row][col] = 0
                return is_solved
    return True

def sudoku(puzzle):
    solve(puzzle)
    return puzzle
