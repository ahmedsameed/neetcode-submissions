class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        count=0
        wordSet=set(wordDict)
        dp={}
        def dfs(remain):

            #print("L6")
            #print(remain)
            if len(remain)==0:
                #print("L9")
                return True
            if remain in dp:
                return dp[remain]
            for i in range (1,len(remain)+1):


                if remain[:i] in wordSet:
                    #print(14)
                    #print(remain[:i])
                    #print(remain[i:])
                    if dfs(remain[i:]):
                        #print(16)
                        #print(remain[i:])
                        dp[remain]=True
                        return True
            dp[remain]=False
            return False
                


        return dfs(s)