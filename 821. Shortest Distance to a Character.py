# Runtime: 84 ms, faster than 19.14% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 14.5 MB, less than 6.82% of Python3 online submissions for Shortest Distance to a Character.

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [i for i,v in enumerate(s) if v==c]

        return [min(list(map(lambda x:abs(x-i), indices))) for i in range(len(s))]
