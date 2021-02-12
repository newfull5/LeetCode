class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        
        for i in range(len(nums)):
            a = nums[i]
            
            if i == 0:
                answer.append(a)
            else:
                answer.append(answer[-1]+a)
                
        return answer
