class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        cur=[]
        def dfs(closedN,openN):
            if closedN == openN ==n:
                res.append("".join(cur))
            
            if openN<=n:
                cur.append("(")
                dfs(closedN,openN+1)
                cur.pop()

            if closedN<openN:
                cur.append(")")
                dfs(closedN+1,openN)
                cur.pop()
        dfs(0,0)
        return res


        