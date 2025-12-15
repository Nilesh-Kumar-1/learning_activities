# Valid Sudoku
# Solved 
# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

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

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_len = 9
        col_len = 9
        box_len = 3

        for i in range(row_len):
            row_set = set()
            for j in range(col_len):
                if board[i][j] in row_set:
                    return False
                if board[i][j] != '.' and board[i][j] not in row_set:
                    row_set.add(board[i][j])
        
        for i in range(col_len):
            col_set = set()
            for j in range(row_len):
                if board[j][i] in col_set:
                    return False
                if board[j][i] != '.' and board[j][i] not in col_set:
                    col_set.add(board[j][i])
        
        for square in range(0,9):
            box_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in box_set:
                        return False
                    if board[row][col] != '.' and board[row][col] not in box_set:
                        box_set.add(board[row][col])
        return True
                    

# Bit manipulation solution using bitmask
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True

board=[[".",".",".",".","5",".",".","1","."],
       [".","4",".","3",".",".",".",".","."],
       [".",".",".",".",".","3",".",".","1"],
       ["8",".",".",".",".",".",".","2","."],
       [".",".","2",".","7",".",".",".","."],
       [".","1","5",".",".",".",".",".","."],
       [".",".",".",".",".","2",".",".","."],
       [".","2",".","9",".",".",".",".","."],
       [".",".","4",".",".",".",".",".","."]]
sol = Solution()
print(sol.isValidSudoku(board))  # Output: True

print(1<<-1)  # Output: 4
print(1<<3)  # Output: 8