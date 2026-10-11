class Solution:
    def numDecodings(self, s: str) -> int:

        dp=[-1]*len(s)
        def dfs(i):
            if i==len(s):
                return 1

            if s[i]=="0":
                return 0
            if dp [i]!=-1:
                return dp[i]
                
            ways=dfs(i+1)
            # 1 3 4
            #take 1

            if i+1<len(s):
                #check if we can take two
                num=int(s[i:i+2])
                if 10<=num<=26:
                    ways+=dfs(i+2)

            dp[i]=ways
            return ways
        
        return dfs(0)
