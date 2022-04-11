# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        tmp = head
        num_of_head = 0
        while tmp != None:
            tmp = tmp.next
            num_of_head = num_of_head + 1

        rtn_head = head
        for i in range(num_of_head // 2):
            rtn_head = rtn_head.next

        return rtn_head