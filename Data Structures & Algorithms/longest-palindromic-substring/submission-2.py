class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxv=0
        res=""
        dp=[[None]*len(s) for i in range(len(s))]

        def dfs(i,j):
            if i>=j:
                return True
            if dp[i][j] is not None:
                return dp[i][j]
            if s[i]==s[j] and dfs(i+1,j-1):
                dp[i][j]=True
            else:
                dp[i][j]=False    
            return dp[i][j]        
        res=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dfs(i,j) and j-i+1>len(res):
                    res=s[i:j+1]
        return res