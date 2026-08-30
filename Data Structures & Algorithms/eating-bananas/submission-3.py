class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        res=1000
        restime=1000
        while left<=right:
            mid=(left+right)//2
            totaltime=0
            for pile in piles:
                totaltime+=math.ceil(float(pile)/mid)
            if totaltime<=h:
                restime=totaltime
                res=mid
            if totaltime<=h:
                right=mid-1
            elif totaltime>h:
                left=mid+1
        return res

              



        