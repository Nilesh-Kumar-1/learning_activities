def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)] #key = (rows//3 + cols//3)


    for row in range(9):
        for col in range(9):

            square_index = (row//3)*3 + (col//3)
            if board[row][col] == '.':
                continue
            elif (board[row][col] in rows[row]) or (board[row][col] in cols[col]) or (board[row][col] in squares[square_index]):
                return False
            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            squares[square_index].add(board[row][col])
    return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
# Output: true                          