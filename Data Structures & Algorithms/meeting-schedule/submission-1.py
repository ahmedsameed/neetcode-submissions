"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        if not intervals:
            return True
        prevend=intervals[0].end
        for i in range(1,len(intervals)) :
            if prevend > intervals[i].start:
                return False
            prevend=intervals[i].end
        return True

