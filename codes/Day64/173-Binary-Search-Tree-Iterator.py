# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        if root:
            self.stack.append([root, 0])
    
    def next(self) -> int:
        while True:
            node, count = self.stack.pop()
            if count == 0:
                if node.right:
                    self.stack.append([node.right, 0])
                self.stack.append([node, count + 1])
                if node.left:
                    self.stack.append([node.left, 0])
            elif count == 1:
                return node.val
            else:
                print("next error in BSTIterator.")
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()