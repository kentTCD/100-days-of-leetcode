# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None : return head
        tmp = head
        list_node = ListNode(head.val)
        i = 0
        while tmp != None:
            if i != 0:
                list_node = ListNode(tmp.val, list_node)
            tmp = tmp.next
            i = i + 1
        return list_node