class Solution:
    import heapq
    def maxProfit(self, prices: List[int]) -> int:
        heap = []

        answer = 0

        for num in prices:
            heapq.heappush(heap, num)
            if answer < (num - heap[0]):
                answer = (num - heap[0])

        return answer
        
