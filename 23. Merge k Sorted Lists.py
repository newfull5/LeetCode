# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        
        for l in lists:
            while True:
                if l == None:
                    break
                arr.append(l.val)
                l = l.next
                
        arr = sorted(arr, reverse = True)
        
        if not arr:
            return None
        
        for i in range(len(arr)):
            if i == 0:
                answer = ListNode(arr[i])
            else:
                answer = ListNode(arr[i], answer)
                
        return answer
