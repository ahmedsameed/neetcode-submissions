class LL:
    def __init__(self, key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=0
        self.capacity=capacity
        self.keytonode={}
        self.left=LL(0,0)
        self.right=LL(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre

        
    def insert(self,node):
        temp = self.right.prev
        self.right.prev = node 
        node.next = self.right
        temp.next = node 
        node.prev= temp

    
    def get(self, key: int) -> int:

        if key in self.keytonode:
            self.remove(self.keytonode[key])
            self.insert(self.keytonode[key])
            return self.keytonode[key].val     
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.keytonode:
            self.keytonode[key].val=value
            self.remove(self.keytonode[key])
            self.insert(self.keytonode[key])
            return 
        self.new=LL(key,value)
        self.keytonode[key]=self.new
        self.insert(self.new)
        
        if len(self.keytonode) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.keytonode[lru.key]
        
