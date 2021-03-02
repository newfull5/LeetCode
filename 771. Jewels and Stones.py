class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0

        for je in jewels:
            answer += stones.count(je)
        return answer
