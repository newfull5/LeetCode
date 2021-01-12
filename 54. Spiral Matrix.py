class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        import numpy as np
        matrix = np.array(matrix)

        answer = []

        while list(matrix):

            try:
                answer += list(matrix[0])
                matrix = matrix[1:]

                answer += list(matrix[:,-1])
                matrix = matrix[:,:-1]

                answer += list(matrix[-1])[::-1]
                matrix = matrix[:-1]

                answer += list(matrix[:,0])[::-1]
                matrix = matrix[:,1:]
                
            except IndexError:
                break

        return answer
