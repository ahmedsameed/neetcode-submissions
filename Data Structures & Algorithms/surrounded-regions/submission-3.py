class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row=len(board)
        col=len(board[0])
        visit=set()

       

        direction=[[1,0],[0,-1],[-1,0],[0,1]]
        def dfs(i,j):
            if (i,j) in visit:
                return
            visit.add((i,j))

            for dr,dc in direction:
                nr=i+dr
                nc=j+dc
                if nr>=0 and nr<row and nc>=0 and nc<col and (nr,nc) not in visit and board[nr][nc]=="O":
                    dfs(nr,nc)

        for i in range(row):
            for j in range(col):
                if (i==0 or i==row-1 or j==0 or j==col-1) and board[i][j]=="O":
                    dfs(i,j)
                
        
        for r in range(row):
            for c in range(col): 
                if board[r][c] =="O" and (r,c) not in visit : 
                    board[r][c] = "X"









        