class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        l=0
        cursum=0
        res=100001
        for r in range(len(nums)):
            cursum+=nums[r]

            while cursum>=target:
                res=min(res,r-l+1)
                cursum-=nums[l]
                l=l+1
        if res==100001:
            return 0
        return res


        