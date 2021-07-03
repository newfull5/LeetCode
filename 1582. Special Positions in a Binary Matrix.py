# Runtime: 256 ms, faster than 14.72% of Python3 online submissions for Special Positions in a Binary Matrix.
# Memory Usage: 31.4 MB, less than 6.25% of Python3 online submissions for Special Positions in a Binary Matrix.  

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        import numpy as np

        mat = np.matrix(mat)

        answer = 0

        for i in range(len(mat)):

            if 1 == np.sum(mat[i]):
                j = np.matrix.tolist(mat[i])[0].index(1)
                if 1 == np.sum(mat[:,j]):
                    answer += 1

        return answer
