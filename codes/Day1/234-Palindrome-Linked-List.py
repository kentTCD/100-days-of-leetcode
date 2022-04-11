# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        tmp = head
        while tmp != None:
            list.append(tmp.val)
            tmp = tmp.next
        bool = False
        head_len = len(list)
        if head_len == 1:
            bool = True
        else:
            i = 1
            front_half = []
            rear_half = []
            if head_len % 2 == 0:
                prev_cent_head = head_len / 2
                for num in list:
                    if i <= prev_cent_head:
                        front_half.append(num)
                    elif i > prev_cent_head:
                        rear_half.append(num)
                    i = i + 1
                rear_half.reverse()
                if front_half == rear_half:
                    bool = True
            elif head_len % 2 == 1:
                prev_cent_head = head_len // 2
                for num in list:
                    if i <= prev_cent_head:
                        front_half.append(num)
                    elif i > prev_cent_head + 1:
                        rear_half.append(num)
                    i = i + 1
                rear_half.reverse()
                if front_half == rear_half:
                    bool = True

        return bool