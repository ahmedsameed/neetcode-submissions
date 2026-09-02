class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            LIS = dfs(i+1, j)  # skip nums[i]

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i+1, i))  # take nums[i]

            dp[i][j] = LIS
            return dp[i][j]
        
        return dfs(0, -1)