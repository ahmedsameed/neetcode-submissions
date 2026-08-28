class Solution:
    def solve(self, board: List[List[str]]) -> None:
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        
        row=len(board)
        col=len(board[0])
        def dfs(i,j):

            board[i][j]="T"
            for dr,dc in direction:
                if i+dr>=0 and i+dr<row and j+dc>=0 and j+dc<col:
                    if board[i+dr][j+dc]=="O":
                        dfs(i+dr,j+dc) 

        for i in range (row):
            for j in range(col):
                if (i==0 or i==row-1 or j ==0 or j==col-1) and board[i][j]=="O":
                    dfs(i,j)

        for i in range (row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"

                




            
        