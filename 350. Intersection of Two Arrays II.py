# 시도 1. 교집합을 찾아야 하니까, 집합 자료형(set)으로 쉽게 풀 수 있지 않을까?

class Solution:
  """
  inputs : [1,2,2,1], [2,2]
  output : [2]
  Expected : [2,2]
  """
  
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
      
# 아 집합 자료형은 중복을 제거하니까 [2,2] 대신 [2] 가 나오는구나. 다른 방법을 사용해야 겠다.

# 시도 2. 선형탐색을 해버리면 되지 않을까? 시간초과가 걸릴려냐??

class Solution:
  """
  inputs : [1,2,2,1], [2]
  output : [2,2]
  Expected : [2]
  """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        
        for num in nums1:
            if num in nums2:
                answer.append(num)
                
        return answer
      
# 아 생각해보니, 같은 원소가 nums1에 두번나오면 nums2의 원소와 중복 집계되는구나. 시간초과 이전에 그냥 알고리즘이 꼬이네,

# 시도 3. nums1 을 집합자료형으로 만들고 각 요소가 nums1, nums2 배열에 몇번 등장하는지 세어보고 그 중 작은 값을 취하면 어떨까?

# Runtime: 80 ms, faster than 11.30% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14.5 MB, less than 10.29% of Python3 online submissions for Intersection of Two Arrays II.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # nums1 을 짋합 자료형으로 만든다(중복이 사라진다)
        nums = set(nums1)
        
        # 정답으로 제출할 answer 배열을 생성한다.
        answer = []
        
        # nums의 원소를 하나씩 순회하며 
        for num in nums:
            
            # 각 원소가 nums1 배열에 몇 번등장하는지, nums2 배열에 몇번 등장하는지를 세어보고, 그중 작은 값을 cnt 변수에 넣는다.
            cnt = min(nums1.count(num), nums2.count(num))
            
            # 만약 cnt가 0 이라면 어느 한 배열에는 num이 등장하지 않았다는 의미가 된다. 그러므로 continue
            if cnt == 0:
                continue
            # 0 이 아니라면, cnt 값 만큼 num을 생성하여 answer에 추가한다.
            else:
                answer += [num] * cnt        
            
        return answer
