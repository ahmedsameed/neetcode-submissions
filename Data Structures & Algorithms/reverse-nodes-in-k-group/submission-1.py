# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grpPrev=dummy

        def kth(grpPrev,k):
            while grpPrev and k>0:
                grpPrev=grpPrev.next
                k-=1
            return grpPrev

        while True:
            kthnode=kth(grpPrev,k)
            if not kthnode:
                break
            grpNext=kthnode.next
            cur=grpPrev.next
            prev=kthnode.next

            while cur!=grpNext:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            tmp=grpPrev.next
            grpPrev.next=kthnode
            grpPrev=tmp
        return dummy.next
    
        


        