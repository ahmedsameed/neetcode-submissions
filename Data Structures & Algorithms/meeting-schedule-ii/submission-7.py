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
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        count=0
        maxval=0
        while i<len(intervals):
            if start[i]<end[j]:
                count=count+1
                maxval=max(count,maxval)
                i=i+1
            else:
                j=j+1
                count=count-1
        return maxval
        