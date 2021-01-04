class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [] or strs == ['']:
            return ''
        
        strs = sorted(strs, key = lambda x: len(x))

        def Check(match: str, i: int) -> bool:
            for s in strs:
                if not match == s[0:i]:
                    return False
            return True

        for i in range(len(strs[0])+1):
            if not Check(strs[0][0:i],i):
                return strs[0][0:i-1]
            
        return strs[0]
