class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)] 
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if word1[i]==word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dfs(i+1,j+1)
            
            res=min(dfs(i+1,j),dfs(i,j+1))
            res=min(res,dfs(i+1,j+1))
            dp[(i,j)]=res+1
            return res+1
        return dfs(0,0)
        