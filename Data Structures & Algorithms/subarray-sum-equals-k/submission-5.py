class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix={0:1}
        CurSum=0
        res=0
        for i in range(len(nums)):
            CurSum=CurSum+nums[i]
            res=res+prefix.get(CurSum-k,0)
            prefix[CurSum]=1+prefix.get(CurSum,0)
        
            


        return res