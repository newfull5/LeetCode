class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        length = len(matrix)

        def GetDistance(x,y):
            for i in range(1, length*3):
                for j in range(0, i+1):
                    try:
                        if matrix[x-(i-j)][y-j] == 0:
                            return i
                    except IndexError:
                        pass

                    try:
                        if matrix[x+(i-j)][y+j] == 0:
                            return i
                    except IndexError:
                        pass

                    try:
                        if matrix[x-(i-j)][y+j] == 0:
                            return i
                    except IndexError:
                        pass

                    try:
                        if matrix[x+(i-j)][y-j] == 0:
                            return i
                    except:
                        pass

        answer = [[0] * len(matrix[0]) for _ in range(length)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    answer[i][j] = GetDistance(i,j)

        return answer
