# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=dummy
        fast=head
        
        i=0
        while n>0:
            fast=fast.next
            n=n-1
        while fast:
            slow=slow.next
            fast=fast.next
        """dummy=ListNode(None)
        dummy.next=head
        prev=dummy
        curr=head
        next=head.next
        while n>1:
            
            temp=curr.next
            prev=curr
            curr=curr.next
            next=temp
            n=n-1
            print(n)
        print(temp.val)
        print(prev.val)
        prev.next=temp

        return head"""
        slow.next=slow.next.next

        return dummy.next
        
        



        