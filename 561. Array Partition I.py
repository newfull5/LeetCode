"""
#Runtime: 264 ms, faster than 69.51% of Python3 online submissions for Array Partition I.
#Memory Usage: 16.7 MB, less than 95.99% of Python3 online submissions for Array Partition I.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return sum([nums[i] for i in range(0,len(nums),2)])
"""
#Runtime: 320 ms, faster than 17.81% of Python3 online submissions for Array Partition I.
#Memory Usage: 15.9 MB, less than 99.92% of Python3 online submissions for Array Partition I.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        import heapq

        answer = 0

        heapq.heapify(nums)

        while nums:
            answer += heapq.heappop(nums)
            heapq.heappop(nums)
            
        return answer
