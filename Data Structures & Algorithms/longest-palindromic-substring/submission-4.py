class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp =[ [None ] * len(s) for i in range(len(s))]
        maxv = 0 
        def dfs (i,j) :
            if i >= j :
                return True
            if dp[i][j] != None :
                return dp[i][j]
            if s[i] == s[j] and dfs(i+1, j-1) :
                dp[i][j] = True 
                return dp[i][j]
            dp[i][j] = False
            return False 

        result=""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(i,j) and maxv < (j-i + 1):

                    maxv=j-i+1
                    result = s[i:j+1]

        return result   

        