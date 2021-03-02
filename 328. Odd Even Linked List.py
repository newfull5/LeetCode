# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        odd = []
        even = []
        
        while True:
            try:
                odd.append(head.val)
                head = head.next

                even.append(head.val)
                head = head.next
                
            except:
                break

        answer = ListNode(even.pop())
        
        while even:
            answer = ListNode(even.pop(), answer)
            
        while odd:
            answer = ListNode(odd.pop(), answer)
            
        return answer
