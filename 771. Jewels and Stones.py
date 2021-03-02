#Runtime: 32 ms, faster than 63.11% of Python3 online submissions for Jewels and Stones.
#Memory Usage: 14.3 MB, less than 13.91% of Python3 online submissions for Jewels and Stones.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0

        for je in jewels:
            answer += stones.count(je)
        return answer
