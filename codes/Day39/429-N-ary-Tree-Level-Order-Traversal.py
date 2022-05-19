"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.res = []
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, stage):
            if not root:
                return
            if len(self.res)-1 < stage:
                self.res.append([root.val])
            else:
                self.res[stage].append(root.val)
            for node in root.children:
                dfs(node, stage+1)
        dfs(root, 0)
        return self.res