class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_ = 0
        answer = 0

        for num in set(nums):
            temp = nums.count(num)
            if temp > max_:
                max_ = temp
                answer = num

        return answer
