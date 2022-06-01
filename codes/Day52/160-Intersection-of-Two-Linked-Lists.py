# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        l1, l2 = headA, headB
        x = None
        while l1 is not None or l2 is not None:
            if l1 == l2:
                return l1
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
            
        return None