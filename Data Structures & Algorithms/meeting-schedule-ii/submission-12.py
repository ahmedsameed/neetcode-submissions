"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startsorted=sorted(interval.start for interval in intervals)
        endsorted=sorted(interval.end for interval in intervals)
        start=0
        end=0
        count=0
        res=0
        while start<len(startsorted):
            if startsorted[start]<endsorted[end]:
                count+=1
                res=max(res,count)
                start+=1
            else:
                count-=1
                end+=1
        return res
            


