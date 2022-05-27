# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        int_1 = int_2 = 0
        i = 0
        while l1 or l2:
            if l1:
                int_1 += l1.val * (10 ** i)
                l1 = l1.next
            if l2:
                int_2 += l2.val * (10 ** i)
                l2 = l2.next
            i += 1
        int_sum = int_1 + int_2

        for i, char in enumerate(list(str(int_sum))):
            if i == 0:
                node = ListNode(int(char), None)
            else:
                node = ListNode(int(char), node)

        return node