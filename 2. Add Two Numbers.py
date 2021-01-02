# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _l1 = []
        _l2 = []
        
        while l1 != None:
            _l1.append(l1.val)
            l1 = l1.next
            
        while l2 != None:
            _l2.append(l2.val)
            l2 = l2.next
            
        temp1 = int(''.join(list(map(str,_l1)))[::-1])
        temp2 = int(''.join(list(map(str,_l2)))[::-1])
        
        temp = list(str(temp1 + temp2))[::-1]
        
        for i in range(len(temp)):
            if i == 0:
                answer = ListNode(val=temp[i])
            else:
                new_node = ListNode(val=temp[i])
                crnt_node = answer
                
                while crnt_node.next != None:
                    crnt_node = crnt_node.next
                crnt_node.next = new_node
                
        return answer
        
