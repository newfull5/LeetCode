# Runtime: 112 ms, faster than 66.38% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.8 MB, less than 90.05% of Python3 online submissions for Minimum Window Substring.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                    
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
                    
        return s[start:end]
