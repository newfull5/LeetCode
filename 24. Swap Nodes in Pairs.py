# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        arr1 = []
        arr2 = []
        
        lists = []
        
        while True:
            arr1.append(head.val)
            head = head.next
            if head == None:
                break
                
            arr2.append(head.val)
            head = head.next
            if head == None:
                break
        
        for i in range(max(len(arr1),len(arr2))):
            try:
                lists.append(arr2[i])
                lists.append(arr1[i])
            except IndexError:
                lists.append(arr1[i])
        
        answer = ListNode(lists.pop())
        
        while lists:
            answer = ListNode(lists.pop(), answer)
            
        return answer
