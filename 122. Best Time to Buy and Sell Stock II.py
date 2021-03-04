# Runtime: 60 ms, faster than 76.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.
# Memory Usage: 15 MB, less than 67.47% of Python3 online submissions for Best Time to Buy and Sell Stock II.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(len(prices)-1):
            answer += max(0, prices[i+1] - prices[i])
        return answer
