# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        exists = []
        res_head = head
        while head and head.next:
            exists.append(head.val)
            while exists[-1] == head.next.val:
                head.next = head.next.next
                if not head.next:
                    return res_head
            head = head.next
        return res_head