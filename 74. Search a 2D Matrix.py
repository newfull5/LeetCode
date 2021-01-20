"""
#faster than 25.34%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
"""

#faster than 62.63%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if (target <= matrix[i][-1]):
                for j in range(len(matrix[0])):
                    if target == matrix[i][j]:
                        return True
                return False
