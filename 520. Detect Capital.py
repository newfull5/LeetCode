# Runtime: 32 ms, faster than 53.19% of Python3 online submissions for Detect Capital.
# Memory Usage: 14.3 MB, less than 15.57% of Python3 online submissions for Detect Capital.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word[0].upper() + word[1:].lower()
