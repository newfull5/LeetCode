class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import re

        q = re.compile('\d')

        for a,b in [(0,3),(3,6),(6,9)]:
            for c,d in [(0,3),(3,6),(6,9)]:
                temp = sum(list(map(list, zip(*board[a:b])))[c:d], [])
                temp = q.findall(''.join(temp))
                if len(temp) != len(set(temp)):
                    return False

        for i in range(9):
            temp = q.findall(''.join(board[i]))
            if len(temp) != len(set(temp)):
                return False

        board = list(map(list, zip(*board)))

        for i in range(9):
            temp = q.findall(''.join(board[i]))
            if len(temp) != len(set(temp)):
                return False
            
        return  True
