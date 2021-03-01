#Runtime: 52 ms, faster than 82.51% of Python3 online submissions for Trapping Rain Water.
#Memory Usage: 14.8 MB, less than 68.24% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: List[int]) -> int:
        def solution(height, answer):

            left = None

            for i in range(len(height)):
                if left == None and height[i] != 0:
                    left = i

            while True:
                try:
                    for i in range(left+1, len(height)+10):
                        if height[i] >= height[left]:
                            answer += (height[left] * (i-left)) - sum(height[left:i])
                            left = i
                            break

                except IndexError:
                    break

            return answer
        
        if len(height) <=2 :
            return 0

        idx = height.index(max(height))

        answer = 0

        answer = solution(height[:idx+1], answer)
        answer = solution(height[idx:][::-1], answer)
        
        return answer
