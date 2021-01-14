class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals + [newInterval]

        intervals.sort()

        stack = []

        for num in intervals:

            if not stack:
                stack.append(num)

            elif stack[-1][-1] >= num[0]:
                temp = stack.pop()

                stack.append([min(temp[0], num[0]), max(temp[1], num[1])])

            else:
                stack.append(num)
                
        return stack
