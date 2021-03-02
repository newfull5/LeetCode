# Runtime: 504 ms, faster than 77.11% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 18.9 MB, less than 30.84% of Python3 online submissions for Daily Temperatures.

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []

        answer = [0] * len(T)

        for i,v in enumerate(T):

            while stack and T[stack[-1]] < v:
                answer[stack.pop()] = (i - stack[-1])

            stack.append(i)

        return answer
