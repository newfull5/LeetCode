class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def Recul(s):
            for char in sorted(set(s)):
                suffix = s[s.index(char):]

                if set(s) == set(suffix):
                    return char + Recul(suffix.replace(char,''))
            return ''

        return Recul(s)
