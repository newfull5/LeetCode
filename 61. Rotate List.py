# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        from collections import deque
        
        arr = []
        
        while head != None:
            arr.append(head.val)
            head = head.next
            
        k = k % len(arr)
        
        arr = deque(arr)
        
        for _ in range(k):
            temp = arr.pop()
            arr.appendleft(temp)
        
        answer = ListNode(arr.pop(),next=None)
        
        while arr:
            answer = ListNode(arr.pop(), next = answer)
            
        return answer
