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
        ogtocopy={None:None}

        curr=head

        while curr:
            copy=Node(curr.val)
            ogtocopy[curr]=copy
            curr=curr.next
        
        curr=head
        while curr:
            copy=ogtocopy[curr]
            copy.next=ogtocopy[curr.next]
            copy.random=ogtocopy[curr.random]
            curr=curr.next
        return ogtocopy[head]





        