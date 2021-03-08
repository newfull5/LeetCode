# Runtime: 232 ms, faster than 99.11% of Python3 online submissions for Binary Subarrays With Sum.
# Memory Usage: 15.9 MB, less than 59.96% of Python3 online submissions for Binary Subarrays With Sum.

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        answer = 0
        
        if S == 0:
            for arr in ''.join(map(str, A)).split('1'):
                answer += len(arr) * (len(arr)+1) // 2
                
            return answer
        
        A = [1] + A + [1]

        arr = [i for i in range(len(A)) if A[i] == 1]

        for i in range(1, len(arr)-S):
            left = arr[i] - arr[i-1]
            right = arr[i+S] - arr[i+S-1]

            answer += left*right
            
        return answer
