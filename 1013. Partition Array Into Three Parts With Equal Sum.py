# Runtime: 312 ms, faster than 50.26% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum. 
# Memory Usage: 21.2 MB, less than 18.10% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.py

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_ = sum(arr)
        
        if sum_ % 3 != 0:
            return False
        
        total = 0
        target = sum_ // 3
        cnt = 0
        
        for num in arr:
            total += num
            
            if total == target:
                total = 0
                cnt += 1
                
            if cnt == 3:
                return True
            
        return False
