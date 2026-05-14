# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        

        curr=slow.next
        slow.next=None
        prev=slow
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        p1=head
        p2=prev
        while p1 and p2:
            temp=p1.next
            temp2=p2.next
            p1.next=p2
            p2.next=temp
            p1=temp
            p2=temp2
           

