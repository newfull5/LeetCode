class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(10, 27):
            query = str(i) + '#'
            s = s.replace(query, chr(96 + i))

        for i in range(1, 10):
            query = str(i)
            s = s.replace(query, chr(96 + i))

        return s