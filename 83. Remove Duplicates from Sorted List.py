# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        answer = []
        
        while head != None:
            if head.val not in answer:
                answer.append(head.val)
            head = head.next
            
        ans = ListNode(answer.pop())
        
        while answer:
            ans = ListNode(answer.pop(), ans)
            
        return ans
