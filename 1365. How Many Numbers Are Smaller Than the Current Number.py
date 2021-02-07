class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s_nums = sorted(nums)

        diction = {}

        for num in set(nums):
            diction[num] = s_nums.index(num)

        answer = [0] * len(nums)

        for a,b in [(i,v) for i,v in enumerate(nums)]:
            answer[a] = diction[b]

        return answer
