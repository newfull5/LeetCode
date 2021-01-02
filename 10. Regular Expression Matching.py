class Solution:
    import re
    def isMatch(self, s: str, p: str) -> bool:
        p = re.compile(p)
        try:
            return p.search(s).group() == s
        except:
            return False
