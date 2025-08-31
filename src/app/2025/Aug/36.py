'''
36. Valid Sudoku

    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    

    Example 1:


    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

    #########################################################################################
    37. Sudoku Solver
    Hard
    Topics
    premium lock icon
    Companies
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells.

    Example 1:


    Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    Explanation: The input board is shown above and the only valid solution is shown below:

    Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution
'''
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        COLS=[0]*9; ROWS=[0]*9; X=[0]*9
        for z in range(9*9):
            r = z//9; c = z%9
            if board[r][c] == ".": continue
            zz = int(board[r][c])
            x = 3*(r//3)+c//3
            if all(
                [
                    (T[i]|(1<<zz)) == (T[i]^(1<<zz)) for i,T in [(c,COLS),(r,ROWS),(x,X)]
                ]
            ):
                COLS[c]|=(1<<zz)
                ROWS[r]|=(1<<zz)
                X[x]|=(1<<zz)
            else: return False
        return True
    # 37th harder variation of 36th
        def solveSudoku(self, board: List[List[str]]) -> None:
            """
            Do not return anything, modify board in-place instead.
            """
            pass