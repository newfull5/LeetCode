class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = [[a] for a in candidates if a == target]

        candidates = [[a] for a in candidates]
        length = len(candidates)
        arr = []
        
        for _ in range(length+1):
            for i in range(len(candidates)):
                for j in range(i, len(candidates)):
                    temp = (candidates[i] + candidates[j])
                    temp.sort()

                    if sum(temp) == target and temp not in answer:
                        answer.append(temp)

                    elif sum(temp) < target and temp not in candidates:
                        arr.append(temp)

                candidates = arr + candidates

        return answer
