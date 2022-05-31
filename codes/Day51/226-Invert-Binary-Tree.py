# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root:
                return
            left = root.left
            right = root.right

            root.left = right
            root.right = left

            bfs(left)
            bfs(right)

        bfs(root)
        return root