"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        i=0
        j=0 
        count=0
        maxval=0

        start=sorted([interval.start for interval in intervals ])
        end=sorted([interval.end for interval in intervals ])
        
        while i<len(intervals):
            if start[i]<end[j]:
                count=count+1
                maxval=max(maxval,count)
                i=i+1
            else:
                j=j+1
                count-=1
        return maxval