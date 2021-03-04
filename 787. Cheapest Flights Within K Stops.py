# Runtime: 88 ms, faster than 75.25% of Python3 online submissions for Cheapest Flights Within K Stops.
# Memory Usage: 19.9 MB, less than 12.20% of Python3 online submissions for Cheapest Flights Within K Stops.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict
        from heapq import heappush, heappop

        graph = defaultdict(list)

        for a,b,c in flights:
            graph[a].append((b,c))

        Q = [(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v,w in graph[node]:
                    heappush(Q, (price+w, v, k - 1))
        return -1
