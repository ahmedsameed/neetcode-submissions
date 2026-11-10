class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.count=-1

    def next(self, price: int) -> int:
        self.count+=1

        while self.stack and price>=self.stack[-1][1]:
            self.stack.pop()
        res=self.count-self.stack[-1][0] if self.stack else self.count+1
       
        self.stack.append([self.count,price])
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)