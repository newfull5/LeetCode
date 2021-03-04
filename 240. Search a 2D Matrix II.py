"""
# Runtime: 152 ms, faster than 97.87% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.6 MB, less than 31.15% of Python3 online submissions for Search a 2D Matrix II.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if target in arr:
                return True
        return False
"""
    
# Runtime: 168 ms, faster than 52.23% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.7 MB, less than 31.15% of Python3 online submissions for Search a 2D Matrix II.
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any([target in row for row in matrix])
