class Solution:
    def romanToInt(self, s: str) -> int:
        diction = {
            'CM' : 900,
            'CD' : 400,
            'XC' : 90,
            'XL' : 40,
            'IX' : 9,
            'IV' : 4,
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }

        answer = 0

        for num in diction.keys():
            answer += (diction[num]*s.count(num))
            s = s.replace(num*s.count(num), '')

        return answer
