# Runtime: 32 ms, faster than 84.70% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 14.3 MB, less than 86.11% of Python3 online submissions for Unique Number of Occurrences.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        arr = list(Counter(arr).values())

        return len(arr) == len(set(arr))
