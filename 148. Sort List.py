# Runtime: 228 ms, faster than 86.15% of Python3 online submissions for Sort List.
# Memory Usage: 38.1 MB, less than 12.86% of Python3 online submissions for Sort List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        arr = []
        
        while head != None:
            arr.append(head.val)
            head = head.next
            
        arr.sort()
        
        answer = ListNode(arr.pop())
        
        while arr:
            answer = ListNode(arr.pop(), answer)
            
        return answer
