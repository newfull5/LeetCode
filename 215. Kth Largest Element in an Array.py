# Runtime: 64 ms, faster than 72.48% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.1 MB, less than 44.88% of Python3 online submissions for Kth Largest Element in an Array.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        
