# Runtime: 408 ms, faster than 15.47% of Python3 online submissions for Minimum Absolute Difference.
# Memory Usage: 32.8 MB, less than 15.28% of Python3 online submissions for Minimum Absolute Difference.

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        arr = [(arr[i], arr[i+1], arr[i+1]-arr[i]) for i in range(len(arr)-1)]

        min_ = sorted(arr, key = lambda x: x[-1])[0][-1]

        return [[a,b] for a,b,c in arr if c == min_]
