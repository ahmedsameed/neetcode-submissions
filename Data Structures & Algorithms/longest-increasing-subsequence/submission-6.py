class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp=[[-1]*(len(nums)+1) for i in range(len(nums))]
        
        def dfs(i,j):
            if i<0:
                return 0
            if dp[i][j+1]!=-1:
                return dp[i][j+1]
            LIS=dfs(i-1,j)

            if j==-1 or nums[i]<nums[j]:
                LIS=max(LIS,1+dfs(i-1,i))
            dp[i][j+1]=LIS
            return LIS

        return dfs(len(nums)-1,-1)    
                    