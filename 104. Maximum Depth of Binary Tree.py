# Runtime: 36 ms, faster than 92.25% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.3 MB, less than 97.45% of Python3 online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        arr = [root]

        cnt = 0

        while arr:
            temp = []
            cnt += 1

            for node in arr:
                l = node.left
                r = node.right
                if l != None:
                    temp.append(l)
                if r != None:
                    temp.append(r)

            arr = temp[:]

        return cnt
        
