class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        column=set()
        posd=set()
        negd=set()
        board=[["."] * n for i in range(n)]

        def dfs(i):
            if i==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in column or (i+c) in posd or (i-c) in negd:
                    continue
                column.add(c)
                posd.add(i+c)
                negd.add(i-c)
                board[i][c]="Q"
                dfs(i+1)
                
                column.remove(c)
                posd.remove(i+c)
                negd.remove(i-c)
                board[i][c]="."

        dfs(0)

        return res