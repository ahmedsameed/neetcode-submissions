class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        res=0
        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            dp.append(row)
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    res=res+1
        return res
        
        