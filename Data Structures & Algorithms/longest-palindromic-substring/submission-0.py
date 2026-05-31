class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        residx=0
        resLen=0
        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(False)
            dp.append(row)
        for i in range(len(s)):
            for j in range(len(s)):
                dp[i][j]=False

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if resLen<j-i+1:
                        resLen=j-i+1
                        residx=i
        return s[residx:residx+resLen]
                



        