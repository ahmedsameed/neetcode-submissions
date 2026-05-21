class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #so we need the rate to be min
        #brute force: trail and error 
        #min rate would be 1 and max rate could be max no of pile monkey can eat in an hour
        #run the array through every rate starting from 0 to max and whichever gives the answer first that is out minrate.
        #optimization Use binary search to earch throught the rate. if no of hours < h for a rate check its left side.
        maxp=0
        for i in range(0,len(piles)):
            maxp=max(maxp,piles[i])
        start=1
        end=maxp
        res=end
        while start<=end:
            k=(start+end)//2
            time=0
            for i in range(len(piles)):
                time=time+math.ceil(float(piles[i])/k)
            if time <=h:
                res=k
                end=k-1
            else:
                start=k+1
        return res
