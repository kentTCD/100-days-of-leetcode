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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def isConnected(root,head): ##checks if linked list is in the tree
            if head is None: #when linked list ends, it is there! 
                return True
            
            if root is None: #when root ends
                return root == head
            
            if root.val != head.val: #value not equal 
                return False
            
            # check left and right subtree
            return isConnected(root.left,head.next) or isConnected(root.right,head.next)
        
        
        def helper(root):
            if not root:
                return False
            
            if root.val == head.val: ##if a values matches, check down the path
                if isConnected(root,head):
                    return True
                    
            # go through left and right subtree
            return helper(root.left) or helper(root.right)
        
        
        return helper(root)