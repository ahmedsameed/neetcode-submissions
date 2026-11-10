class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curmax=1
        curmin=1
        res=nums[0]
        for i in range(len(nums)):        
            candidates=(nums[i],nums[i]*curmin,nums[i]*curmax)

            curmax=max(candidates)
            curmin=min(candidates)
            
            res=max(curmax,res)
            
        return res