class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []

        threshold = len(nums)/3

        setnums = set(nums)

        for num in setnums:
            if nums.count(num) > threshold:
                answer.append(num)

        return answer
