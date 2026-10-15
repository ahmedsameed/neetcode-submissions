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
        print(start)

        end=sorted([i.end for i in intervals])
        print(end)
        i=0
        j=0
        count=0
        maxv=0
        while i<=len(start)-1:
            if start[i]<end[j]:
                count=count+1
                i=i+1
            else:
                count=count-1
                j=j+1
            maxv=max(maxv,count)
        return maxv
        