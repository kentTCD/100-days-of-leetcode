# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        info = []
        leng = 0
        while head:
            info.append(head)
            head = head.next
            leng += 1

        front = info[:leng//2]
        rear  = info[leng//2:]
        
        for i, f in enumerate(front):
            f.next = info[leng-1 - i]
        
        for i, r in enumerate(reversed(rear)):
            if i == len(rear)-1:
                r.next = None
            else:
                r.next = info[i+1]