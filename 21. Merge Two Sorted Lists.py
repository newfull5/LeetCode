# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lists = []
        
        while l1 != None:
            lists.append(l1.val)
            l1 = l1.next
        
        while l2 != None:
            lists.append(l2.val)
            l2 = l2.next
            
        if not lists:
            return None
        
        lists = sorted(lists, reverse = True)
        
        for i in range(len(lists)):
            if i == 0:
                newNode = ListNode(lists[i])
            else:
                newNode = ListNode(lists[i],newNode)
        return newNode
