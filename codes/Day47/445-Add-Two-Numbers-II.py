# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traversal(head):
            val = 0
            cur = head
            while cur:
                val = val * 10 + cur.val
                cur = cur.next
            return val
        res = traversal(l1) + traversal(l2)
        prev = None
        if res == 0:
            return ListNode(res)
        while res > 0:
            num = res%10
            Node = ListNode(num,prev)
            prev = Node
            res = res//10
        return prev