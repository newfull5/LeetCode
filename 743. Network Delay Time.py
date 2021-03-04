# Runtime: 488 ms, faster than 50.30% of Python3 online submissions for Network Delay Time.
# Memory Usage: 16.2 MB, less than 51.68% of Python3 online submissions for Network Delay Time.


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        from heapq import heappop, heappush

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        Q = [(0,k)]

        dist = defaultdict(int)

        while Q:
            time, node = heappop(Q)
            if node not in dist:
                dist[node] = time

                for v, w in graph[node]:
                    heappush(Q, (time + w, v))

        if len(dist) == n:
            return (max(dist.values()))
        return -1
        
