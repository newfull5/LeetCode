# Runtime: 228 ms, faster than 5.44% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 15.6 MB, less than 5.72% of Python3 online submissions for Reconstruct Itinerary.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        answer = []

        def DFS(path, rest):
            if answer:
                return

            if not rest:
                answer.append(path)
                return

            for arr in rest:
                if path[-1] == arr[0]:
                    copy = rest[:]
                    copy.remove(arr)

                    DFS(path + [arr[1]], copy)

        DFS(['JFK'], tickets)

        return sorted(answer, key = lambda x: x[1:])[0]
