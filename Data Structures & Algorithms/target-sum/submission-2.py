class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(i,sum):

            if (i,sum) in dp:
                return dp[(i,sum)]
            if sum==target and i==len(nums):
                return 1

            if i>len(nums)-1:
                return 0


            
            dp[(i,sum)]=dfs(i+1,sum-nums[i]) + dfs(i+1,sum+nums[i])
            return dp[(i,sum)]

        return dfs(0,0)
        