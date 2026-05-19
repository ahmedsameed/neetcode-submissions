# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def getkth(groupprev):
            n=0
            while groupprev and k>n:
                n=n+1
                groupprev=groupprev.next
            return groupprev
        
        dummy=ListNode()
        dummy.next=head
        groupprev=dummy

        while True:
            print("Ahmed")
            kth=getkth(groupprev)
            


            if not kth:
                break
            groupNext=kth.next
            prev=groupNext
            curr=groupprev.next
            while curr!=groupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            temp=groupprev.next
            groupprev.next=kth
            groupprev=temp
        return dummy.next

            




        