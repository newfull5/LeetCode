# Runtime: 40 ms, faster than 47.23% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 14.1 MB, less than 88.26% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)):
            if nums1[i] == 0 and nums2:
                nums1[i] = nums2.pop()
                
        nums1.sort()
