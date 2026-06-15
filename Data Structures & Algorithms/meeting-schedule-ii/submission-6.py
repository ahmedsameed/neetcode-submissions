"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        #(0,5,15)
        #(40,10,20)
        i=0
        j=0
        count=0
        maxc=0
        while i<len(start) :
            print(j)
            if start[i]<end[j]:
                count=count+1
                
                i=i+1
            else:
                count=count-1
                j=j+1
            maxc=max(maxc,count)

        return maxc
