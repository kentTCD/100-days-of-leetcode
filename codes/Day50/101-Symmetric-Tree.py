# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        memo = {}
        def bfs(root, depth):
            root_val = root.val if root else None
            if memo.get(depth):
                memo[depth].append(root_val)
            else:
                memo[depth] = [root_val]

            if not root:
                return

            bfs(root.left, depth+1)
            bfs(root.right, depth+1)

        bfs(root, 0)
        print(memo)
        for depth, row in memo.items():
            if depth == 0:
                continue
            len_row = len(row)
            if len_row % 2 == 1:
                return False
            if row[:len_row//2] != list(reversed(row[len_row//2:])):
                return False
        return True