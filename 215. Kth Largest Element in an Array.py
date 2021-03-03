"""
# Runtime: 64 ms, faster than 72.48% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.1 MB, less than 44.88% of Python3 online submissions for Kth Largest Element in an Array.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
"""

# Runtime: 64 ms, faster than 72.48% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15 MB, less than 93.30% of Python3 online submissions for Kth Largest Element in an Array.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappop, heapify

        nums = list(map(lambda x: x*-1, nums))

        heapify(nums)

        for _ in range(k-1):
            heappop(nums)

        return heappop(nums) * -1        
