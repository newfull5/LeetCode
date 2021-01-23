class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        stack = []

        if not stack:
            stack.append(nums.pop())


        answer = []

        while nums:

            if stack[-1] - nums[-1] == 1:
                stack.append(nums.pop())

            elif stack[-1] - nums[-1] != 1:
                if len(stack) != 1:
                    answer.append(f'{stack[-1]}->{stack[0]}')

                else:
                    answer.append(str(stack[0]))

                stack = []

                stack.append(nums.pop())

        if stack:
            if len(stack) != 1:
                answer.append(f'{stack[-1]}->{stack[0]}')
            else:
                answer.append(str(stack[0]))

        answer.reverse()
        
        return answer
