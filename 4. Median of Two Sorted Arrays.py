class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2
        temp.sort()
        if len(temp) % 2 == 0:
            return ((temp[len(temp)//2] + temp[-1+len(temp)//2]) / 2)
        else:
            return (temp[len(temp)//2])
