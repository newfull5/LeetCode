class Solution:
    def countAndSay(self, n: int) -> str:
        def Recul(string, n):
            if n == 1:
                return string
            answer = ''

            i = 0
            for j in range(len(string)):
                if string[i] != string[j]:
                    answer += f'{j-i}{string[i]}'
                    i = j

            answer += f'{len(string)-i}{string[i]}'

            return Recul(answer, n-1)
        
        return Recul('1',n)
