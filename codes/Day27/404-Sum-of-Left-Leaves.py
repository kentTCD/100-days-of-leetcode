# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
global_sum = 0
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        global global_sum
        global_sum = 0
        
        def recursion(root, l_or_r):
            if root:
                if l_or_r == 'left' and not(root.left or root.right):
                    global global_sum
                    global_sum += root.val
                recursion(root.right, 'right')
                recursion(root.left, 'left')
        recursion(root, 'start')
        return global_sum