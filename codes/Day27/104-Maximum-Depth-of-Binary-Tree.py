# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_height = 0
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cur_height = 0
        global max_height
        max_height = 0
        
        def recursion(root, cur_height):
            if root:
                cur_height += 1
                global max_height
                max_height = max(cur_height, max_height)
                recursion(root.right, cur_height)
                recursion(root.left, cur_height)
        recursion(root, cur_height)
        return max_height