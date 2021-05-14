# Runtime: 2152 ms, faster than 5.02% of Python3 online submissions for Assign Cookies.
# Memory Usage: 15.6 MB, less than 98.98% of Python3 online submissions for Assign Cookies.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        s.sort()
        g.sort()

        for _ in range(min(len(g),len(s))):

            cookie = s.pop()

            for i in range(len(g)-1,-1,-1):
                greed_factor = g[i]

                if greed_factor <= cookie:
                    g = g[:i] + g[i+1:]
                    answer += 1
                    break

        return answer
        
