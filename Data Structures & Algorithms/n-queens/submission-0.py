class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        columns=set()
        posdiag=set()
        negdiag=set()
        board=[["."] * n for i in range(n)]
        def dfs(i):
            if i==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in columns or (i+c) in posdiag or (i-c) in negdiag:
                    continue
                columns.add(c)
                posdiag.add(i+c)
                negdiag.add(i-c)
                board[i][c]="Q"

                dfs(i+1)

                columns.remove(c)
                posdiag.remove(i+c)
                negdiag.remove(i-c)
                board[i][c]="."
        dfs(0)
        return res



        