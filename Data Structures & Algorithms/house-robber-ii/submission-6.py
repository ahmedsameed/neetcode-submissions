class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        dp=[[-1]*len(nums) for i in range(2)]
        def dfs(n,i):
            if n==i:
                return nums[i]
            if n<i:
                return 0
            if dp[i][n]!=-1:
                return dp[i][n]
            dp[i][n]=max(nums[n]+dfs(n-2,i),dfs(n-1,i))
            return dp[i][n]





        return max(dfs(len(nums)-1,1),dfs(len(nums)-2,0))        #1 2 3
        #2 3 1


