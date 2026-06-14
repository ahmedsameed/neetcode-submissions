class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res=[intervals[0]]

        for start,end in intervals[1:]:
            prevend = res[-1][1]
            if start<=prevend:
                res[-1][1]=max(end,prevend)
            else:
                res.append([start,end])
        return res
        