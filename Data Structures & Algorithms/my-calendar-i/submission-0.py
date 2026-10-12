from sortedcontainers import SortedList

class MyCalendar:
    
    def __init__(self):
        self.events=SortedList()
      
        

    def book(self, startTime: int, endTime: int) -> bool:
        def binarysearch(starttime):
            left=0
            right=len(self.events)-1
            val=0
            while left<=right:
                mid=(left+right)//2
                
                if self.events[mid][0]==starttime:
                    return val
                if self.events[mid][0]<starttime:
                    left=mid+1
                else:
                    right=mid-1
            return left
        if len(self.events)>0:        
            idx=binarysearch(startTime)
            if idx>0 and self.events[idx-1][1]>startTime:
                return False
            if idx<len(self.events) and self.events[idx][0]<endTime:
                return False
            
        self.events.add((startTime,endTime))
        return True




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)