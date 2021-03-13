# Runtime: 6236 ms, faster than 7.02% of Python3 online submissions for 3Sum.
# Memory Usage: 18.1 MB, less than 25.59% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answer = []

        length = len(nums)

        for i in range(1, len(nums)):
            current = nums[i-1]
            copy = nums[i:]
            left, right = 0, length-i-1

            while left < right:
                sum_ = current + copy[left] + copy[right]
                if sum_ == 0:
                    temp = sorted([current, copy[left], copy[right]])
                    if temp not in answer:
                        answer.append(temp)
                    left += 1

                elif sum_ > 0:
                    right -= 1

                elif sum_ < 0:
                    left += 1

        return answer
