# Runtime: 216 ms, faster than 90.12% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
# Memory Usage: 17.9 MB, less than 68.83% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import Counter
        
        time = list(map(lambda x: x%60,time))

        time = Counter(time)

        answer = 0

        visited = []

        for num,cnt in time.items():

            if num in visited:
                continue

            if num == 30 or num == 0:
                # Combination (nCr)
                answer += cnt * (cnt-1) // 2

            else:
                answer += cnt * time[60-num]
                visited.append(60-num)
                
        return answer
