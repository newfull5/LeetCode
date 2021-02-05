# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        lists = []
        
        while head != None:
            if head.val != val:
                lists.append(head.val)
            head = head.next
            
        if not lists:
            return None
        
        answer = ListNode(lists.pop(), None)
        
        while lists:
            answer = ListNode(lists.pop(), answer)
            
        return answer
