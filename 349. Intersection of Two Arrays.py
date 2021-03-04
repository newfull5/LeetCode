# Runtime: 48 ms, faster than 54.20% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.4 MB, less than 47.50% of Python3 online submissions for Intersection of Two Arrays.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
