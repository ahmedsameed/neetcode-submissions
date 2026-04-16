class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # MaxAr=0
        # lenh=len(heights)
        # for i in range(lenh):
        #     for j in range(i,lenh):
        #         heightmin=min(heights[i],heights[j])
        #         Area=heightmin*(j-i)
        #         MaxAr=max(MaxAr,Area)
        # return MaxAr
        
        MaxAr=0
        lenh=len(heights)
        l=0
        r=lenh-1

        while l<r:
            MaxAr=max(MaxAr,(r-l)*min(heights[r],heights[l]))
            print(r)
            print(l)
            if heights[r]>=heights[l]:
                l=l+1
                continue
            if heights[r]<heights[l]:
                
                r=r-1
                continue
            
        return MaxAr

