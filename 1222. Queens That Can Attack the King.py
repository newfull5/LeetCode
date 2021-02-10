class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def leftdown(a, b):
            if a == -1 or b == -1:
                return 

            if [a,b] in queens:
                return [a,b]

            return leftdown(a-1, b-1)

        def leftup(a, b):
            if a == 8 or b == -1:
                return 

            if [a,b] in queens:
                return [a,b]

            return leftup(a+1, b-1)

        def rightup(a, b):
            if a == 8 or b == 8:
                return 

            if [a,b] in queens:
                return [a,b]

            return rightup(a+1, b+1)

        def rightdown(a, b):
            if a == -1 or b == 8:
                return 

            if [a,b] in queens:
                return [a,b]

            return rightdown(a-1, b+1)

        answer = []

        try: 
            answer.append(sorted([[a,b] for a,b in queens if b == king[1] and a < king[0]])[-1]) 
        except: 
            pass

        try:
            answer.append(sorted([[a,b] for a,b in queens if b == king[1] and a > king[0]])[0])
        except:
            pass

        try: 
            answer.append(sorted([[a,b] for a,b in queens if a == king[0] and b < king[1]])[-1])
        except: 
            pass

        try:
            answer.append(sorted([[a,b] for a,b in queens if a == king[0] and b > king[1]])[0])
        except:
            pass

        answer.append(leftup(king[0],king[1]))

        answer.append(rightup(king[0],king[1]))

        answer.append(leftdown(king[0],king[1]))

        answer.append(rightdown(king[0],king[1]))

        return [arr for arr in answer if arr]
