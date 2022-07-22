# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Sum up from root to each depth and check if it's equal to targetSum
        def dfs_calc_sum(root, path):
            if not root:
                return
            path += root.val
            if path == targetSum:
                nonlocal sum_count
                sum_count += 1
            dfs_calc_sum(root.left, path)
            dfs_calc_sum(root.right, path)

        # Send each node to dfs_calc_sum function
        def patrol(root):
            if not root:
                return
            dfs_calc_sum(root, 0)
            patrol(root.left)
            patrol(root.right)

        sum_count = 0
        patrol(root)
        return sum_count