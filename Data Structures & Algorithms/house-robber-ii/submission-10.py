class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp1=[-1]*(len(nums))
        dp0=[-1]*(len(nums))
        def dfs(n,i):

            if n<i:
                return 0
            if i==0:
                if dp0[n]!=-1:
                    return dp0[n]
            else:
                if dp1[n]!=-1:
                    return dp1[n]
            if i==0:
                dp0[n]=max(nums[n]+dfs(n-2,i),dfs(n-1,i))
                return dp0[n]
            else: 

                dp1[n]=max(nums[n]+dfs(n-2,i),dfs(n-1,i))
                return dp1[n]



        return max(dfs(len(nums)-1,1),dfs(len(nums)-2,0))
        


