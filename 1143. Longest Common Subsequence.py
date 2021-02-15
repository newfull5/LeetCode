class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1) 
        len2 = len(text2) 

        matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)] 

        for i in range(1, len1 + 1): 
            for j in range(1, len2 + 1): 
                if text1[i - 1] == text2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1 
                else: 
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

        return matrix[-1][-1]
