class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        import heapq
        
        nums = list(set(nums))

        heapq.heapify(nums)

        while True:
            if not nums:
                return 1
            
            before = heapq.heappop(nums)
            if before > 0:
                break

        if not nums and before != 1 or before != 1:
            return 1
        
        if not nums and before == 1:
            return 2
            
        for _ in range(len(nums)):
            crt = heapq.heappop(nums)

            if crt - before != 1:
                return (before + 1)
            
            before = crt
            
        return crt + 1
