# Runtime: 196 ms, faster than 68.82% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 16 MB, less than 15.36% of Python3 online submissions for Sum of Square Numbers.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = []

        for i in range(100000):
            if i*i > c:
                break
            arr.append(i*i)

        left = 0
        right = len(arr)-1

        def sol(left, right):
            while left <= right:
                if arr[left] + arr[right] < c:
                    left += 1
                elif arr[left] + arr[right] > c:
                    right -= 1
                else:
                    return True
            return False

        return sol(left,right)
