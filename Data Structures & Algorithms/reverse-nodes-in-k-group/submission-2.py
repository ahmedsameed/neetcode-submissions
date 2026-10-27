# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)
        grpprev=dummy
        def getkth(grpprev,k):
            while grpprev and k>0:
                grpprev=grpprev.next
                k-=1
            return grpprev

        while True:
            getkthnode=getkth(grpprev,k)
            if not getkthnode:
                break
            grpNext=getkthnode.next
            con=grpprev.next
            cur=grpprev.next
            prev=grpprev
            while cur!=grpNext:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            temp=grpprev.next
            con.next=grpNext
            grpprev.next=getkthnode
            grpprev=temp
        return dummy.next
            
        
        