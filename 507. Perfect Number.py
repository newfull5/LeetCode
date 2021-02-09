class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        d = []
        for i in range(1, int(num**0.5)+1):
            if num%i == 0:
                d.append(i)
                if i!=num//i:
                    d.append(num//i)

        return sum(d) == num*2
