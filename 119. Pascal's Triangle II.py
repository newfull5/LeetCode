class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
            arr = []

            for i in range(1, rowIndex+2):
                temp = [0] * i
                temp[0] = 1
                temp[-1] = 1
                arr.append(temp)

            for i in range(1,len(arr)-1):
                for j in range(0, len(arr[i])-1):
                    arr[i+1][j+1] = (arr[i][j] + arr[i][j+1])

            return arr[-1]
