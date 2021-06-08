# Runtime: 336 ms, faster than 20.81% of Python3 online submissions for Subarray Sums Divisible by K.
# Memory Usage: 18.3 MB, less than 32.98% of Python3 online submissions for Subarray Sums Divisible by K.

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        d = [1] + [0] * k 
        acc = 0
        for a in nums:
            acc = (acc + a) % k
            if d[acc]:
                res += d[acc]
            d[acc] += 1            
        return res
