class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)

        dp=[None]*len(s)
        def dfs(i):
            if i==len(s):
                return True
            if  dp[i]!=None:
                return dp[i]
            for j in range(i,len(s)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        dp[i]=True
                        return dp[i]
            dp[i]=False
            return False


        return dfs(0)
    