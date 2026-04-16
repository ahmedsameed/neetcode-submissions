class Solution:
    def maxArea(self, heights: List[int]) -> int:
        MaxAr=0
        lenh=len(heights)
        for i in range(lenh):
            for j in range(i,lenh):
                heightmin=min(heights[i],heights[j])
                Area=heightmin*(j-i)
                MaxAr=max(MaxAr,Area)
        return MaxAr
        