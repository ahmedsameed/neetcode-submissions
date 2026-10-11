class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        wordSet=set(wordDict)
        dp=[None]*len(s)
        def dfs(i):
            if i==len(s):
                return True
            if dp[i] !=None:
                return dp[i]
            for j in range(i,len(s)):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        if j+1<len(s):
                            dp[j+1]=True
                        dp[i]=True
                        return True
            dp[i]=False
            return False


        return dfs(0)
    