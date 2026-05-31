class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
       

       
        def dfs(i,num):
            dp=[-1]*len(nums)
            def helper(i):
                if i>=len(num):
                    return 0
                
                if dp[i]!=-1:
                    return dp[i]
                dp[i]=max(helper(i+1),num[i]+helper(i+2))
                return dp[i]
            return helper(0)
        return max(nums[0],dfs(0,nums[1:]), dfs(0,nums[:-1]))

                
            
                
        