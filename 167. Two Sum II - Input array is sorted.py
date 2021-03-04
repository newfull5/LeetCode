# Runtime: 2600 ms, faster than 5.01% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.9 MB, less than 5.92% of Python3 online submissions for Two Sum II - Input array is sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            find = target - numbers[i]
            if find not in numbers:
                continue
            index = numbers.index(find)

            if index != i:
                return sorted([i+1,index+1])
