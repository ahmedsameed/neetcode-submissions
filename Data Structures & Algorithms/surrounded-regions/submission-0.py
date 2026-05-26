class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row=len(board)
        column=len(board[0])

        def capture(r,c):
            if r==row or c==column or r<0 or c<0 or board[r][c]!="O":
                return 
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        for i in range(row):
            if board[i][0]=="O":
                capture(i,0)
            if board[i][column-1]=="O":
                capture(i,column-1)
        
        for i in range(column):
            if board[0][i]=="O":
                capture(0,i)
            if board[row-1][i]=="O":
                capture(row-1,i)

        for i in range(row):
            for j in range(column):
                if board[i][j]=="O":
                    print(i,j)
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"