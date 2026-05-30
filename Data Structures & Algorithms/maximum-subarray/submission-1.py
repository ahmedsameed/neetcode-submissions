class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum=nums[0]
        CurSum=0

        for i in range(len(nums)):
            if CurSum<0:
                CurSum=0
            CurSum=CurSum+nums[i]
            maxSum=max(maxSum,CurSum)
        return maxSum
        