# Valid Sudoku
# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:



# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example 2:

board=[["1","2",".",".","3",".",".",".","."],
       ["4",".",".","5",".",".",".",".","."],
       [".","9","8",".",".",".",".",".","3"],
       ["5",".",".",".","6",".",".",".","4"],
       [".",".",".","8",".","3",".",".","5"],
       ["7",".",".",".","2",".",".",".","6"],
       [".",".",".",".",".",".","2",".","."],
       [".",".",".","4","1","9",".",".","8"],
       [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

def isValidSudoku(board: list[list[str]]) -> bool:
        def row(board):
            set_row = set()
            for i in board:
                print(i)
                for j in i:
                    if j != '.':
                        if j in set_row:
                            return False
                        set_row.add(j)
                set_row = set()
            return True
        def col(board):
            set_col = set()
            for i in range(9):
                for j in range(9):
                    if board[j][i] != '.':
                        if board[j][i] in set_col:
                            return False
                        set_col.add(board[j][i])
                set_col = set()
            return True
        def boxes(board):
            set_box = set()
            for i in range(0,9,3):
                for j in range(0,9,3):
                    for k in range(3):
                        for l in range(3):
                            if board[i+k][j+l] != '.':
                                if board[i+k][j+l] in set_box:
                                    return False
                                set_box.add(board[i+k][j+l])
                    set_box = set()
            return True
        return row(board) and col(board) and boxes(board)
print(isValidSudoku(board))

# print(set() == set())