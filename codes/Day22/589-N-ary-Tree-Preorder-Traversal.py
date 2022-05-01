"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        rtn_list = []
        def bfs(target_node):
            if not target_node:
                return
            rtn_list.append(target_node.val)
            for node in target_node.children:
                bfs(node)
        bfs(root)
        return rtn_list