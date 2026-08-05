class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i,sum):
            if sum==target and i==len(nums):
                return 1

            if i>len(nums)-1:
                return 0

            res=0

            res=dfs(i+1,sum-nums[i]) + dfs(i+1,sum+nums[i])
            return res

        return dfs(0,0)
        