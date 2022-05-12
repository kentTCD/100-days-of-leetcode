# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.bool = False
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def recursion(root, head_tmp):
            if not head_tmp:
                self.bool = True
                return
            if not root:
                return
            head_tmp = head if head_tmp.val != root.val and head.val == root.val else head_tmp
            head_tmp = head_tmp.next if head_tmp.val == root.val else head
            recursion(root.left, head_tmp)
            recursion(root.right, head_tmp)

        recursion(root, head)
        
        return self.bool