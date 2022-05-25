"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapping = {}
        new_head = Node(head.val)
        mapping[head] = new_head
        p = head
        q = new_head
        while p.next:
            q.next = Node(p.next.val)
            mapping[p.next] = q.next
            p = p.next
            q = q.next
        q.next = None
        
        p = head
        q = new_head
        while p:
            if p.random:
                q.random = mapping[p.random]
            p = p.next
            q = q.next
        return new_head