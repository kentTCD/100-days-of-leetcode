# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ### My solution
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            counter += 1
        for i in range(counter//2):
            head = head.next
        return head

    ### Someone's solution using two-pointers
    def middleNode(self, head):
        fast_pointer=slow_pointer=head
        #fastP moves two steps at a time faster and slowP moves one step at a time
        while fast_pointer and fast_pointer.next is not None:
            fast_pointer=fast_pointer.next.next
            slow_pointer=slow_pointer.next
        return slow_pointer