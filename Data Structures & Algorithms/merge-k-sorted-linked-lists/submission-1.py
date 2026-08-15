# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self,node):
        self.node=node
    def __lt__(self,other):
        return self.node.val<other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        res=ListNode(0)
        cur=res
        for head in lists:
            if head:
                heapq.heappush(heap,NodeWrapper(head))

        while heap:
            nodewrapper=heapq.heappop(heap)
            cur.next=nodewrapper.node
            cur=nodewrapper.node
            if nodewrapper.node.next:
                heapq.heappush(heap,NodeWrapper(nodewrapper.node.next))


        return res.next
        