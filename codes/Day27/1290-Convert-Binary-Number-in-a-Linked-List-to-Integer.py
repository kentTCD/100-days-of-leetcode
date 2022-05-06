# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        str_val = ''
        while head:
            str_val += str(head.val)
            head = head.next
        return int(str_val, 2)