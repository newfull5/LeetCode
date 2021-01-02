class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        answer = 0

        while i != j:
            answer = max((j-i) * min(height[i], height[j]), answer)

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
                
        return answer
