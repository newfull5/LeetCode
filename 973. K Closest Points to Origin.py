# Runtime: 628 ms, faster than 91.80% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.7 MB, less than 88.25% of Python3 online submissions for K Closest Points to Origin.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda x:x[0]**2 + x[1]**2)[:k]
