class ListNode:
    def __init__(self, key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        print(11)
        
class LRUCache:

    def __init__(self, capacity: int):
        self.curcap=0
        self.keytonode={}
        self.capacity=capacity
        self.left=ListNode(0,0)
        self.right=ListNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,Node):
        prev=Node.prev
        next=Node.next
        prev.next=next
        next.prev=prev

    def insert(self,Node):
        prev=self.right.prev
        next=self.right
        Node.next=next
        Node.prev=prev
        prev.next=Node
        next.prev=Node
    
    
    def get(self, key: int) -> int:
        if key in self.keytonode:
            self.remove(self.keytonode[key])
            self.insert(self.keytonode[key])
            return self.keytonode[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keytonode:
            self.remove(self.keytonode[key])
        self.keytonode[key]=ListNode(key,value)
        self.insert(self.keytonode[key])

        if len(self.keytonode)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.keytonode[lru.key]
 

