# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        answer = ListNode(head.val)
        head = head.next
        
        while head is not None:
            answer = ListNode(head.val, answer)
            head = head.next
            
        return answer
