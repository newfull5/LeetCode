class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        team = list(zip(ages,scores))
        team.sort()
        n = len(team)
        
        lis = [team[i][1] for i in range(n)]
        
        for i in range(1,n):
            for j in range(i):
                if team[i][1]>=team[j][1]:
                    lis[i] = max(lis[i],lis[j]+team[i][1])
        
        return max(lis)
