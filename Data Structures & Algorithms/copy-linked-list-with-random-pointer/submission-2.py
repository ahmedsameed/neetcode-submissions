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
        oldtoCopy=collections.defaultdict(lambda:Node(0))
        oldtoCopy[None]=None

        cur=head
        while cur:
            oldtoCopy[cur].val=cur.val
            oldtoCopy[cur].next=oldtoCopy[cur.next]
            oldtoCopy[cur].random=oldtoCopy[cur.random]
            cur=cur.next
        
        return oldtoCopy[head]