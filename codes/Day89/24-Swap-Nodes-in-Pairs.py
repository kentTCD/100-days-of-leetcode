# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        through_flg = False
        origin = head
        while head:
            if not head.next:
                head = head.next
                continue
            second = head.next
            head.next = second.next
            second.next = head
            if through_flg:
                prev_first.next = second
            else:
                origin = second
            prev_first = head
            head = head.next
            through_flg = True

        return origin