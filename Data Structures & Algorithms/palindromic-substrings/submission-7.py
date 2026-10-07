class Solution:
    def countSubstrings(self, s: str) -> int:

        res=0
        dp=[[None]*len(s) for i in range(len(s)) ]
        #dp=[[None]*len(s) for i in range(len(s))]

        def dfs(i,j):
            if i>=j:
                return True
            if dp[i][j] is not None:
                return dp[i][j]

            if s[i]==s[j] and dfs(i+1,j-1):
                dp[i][j]= True
            else:
                dp[i][j]= False
            return dp[i][j]

        
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dfs(i,j):
                    res=res+1
        return res
        