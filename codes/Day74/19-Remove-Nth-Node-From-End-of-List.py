# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow, head_cp = head, head, head
        i = j = 0
        while fast.next:
            fast = fast.next
            if i >= n:
                slow = slow.next
                j += 1
            i += 1
        if i == 0:
            head_cp = None
        elif i == n-1 and j == 0:
            head_cp = head_cp.next
        else:
            slow.next = slow.next.next
        return head_cp