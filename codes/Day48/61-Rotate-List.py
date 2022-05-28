# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_tmp = head
        node_dq = deque()
        node_count = 0
        # Convert node into deque and count nums
        while head_tmp:
            node_dq.append(head_tmp)
            head_tmp = head_tmp.next
            node_count += 1
        if node_count == 0:
            return head

        # If rotate {node_count} times, then there's no change, so dismiss it
        if node_count > k or node_count < k:
            k = k % node_count
        elif node_count == k:
            return head

        # Move end of node_dq to head of node_dq
        for i in range(k):
            last = node_dq.pop()
            node_dq.appendleft(last)

        # Create ListNode based on arranged node_dq
        for i in range(node_count):
            if i == 0:
                node = ListNode(node_dq.pop().val, None)
            else:
                node = ListNode(node_dq.pop().val, node)

        return node