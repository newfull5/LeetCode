class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        import numpy as np
        import sys

        def Check(i,j):
            answerlist = set({'1','2','3','4','5','6','7','8','9'})
            temp = board[0:3] if i < 3 else (board[3:6] if i < 6 else board[6:])
            temp = temp[:,0:3] if j < 3 else (temp[:,3:6] if j < 6 else temp[:,6:])
            temp = temp.flatten()    
            answerlist = answerlist - set(board[i,:]) - set(board[:,j]) - set(temp)
            return answerlist

        board = np.array(board)
        
        while '.' in list(board.flatten()):
            for i in range(9):
                for j in range(9):
                    if board[i,j] == '.':
                        lists = list(Check(i,j))
                        if len(lists) == 1:
                            board[i,j] = lists[0]
