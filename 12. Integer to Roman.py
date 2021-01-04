class Solution:
    def intToRoman(self, num: int) -> str:
        diction = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I'
        }

        answer = ''

        for n in list(diction.keys()):
            for _ in range(3):
                if num >= n :
                    num -= n
                    answer += diction[n]
                else:
                    break
        return answer
