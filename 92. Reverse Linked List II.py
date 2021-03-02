# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        arr = []
        
        while head is not None:
            arr.append(head.val)
            head = head.next
            
        arr = arr[:left-1] + arr[left-1:right][::-1] + arr[right:]
        
        answer = ListNode(arr.pop())
        
        while arr:
            answer = ListNode(arr.pop(), answer)
            
        return answer
