class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        Flag=False

        def dfs(wi,r,c):
            if wi==len(word):
                nonlocal Flag
                Flag=True
                return
            if r>row-1 or r<0 or c<0 or c>col-1 or board[r][c]!=word[wi] or visited[r][c]:
                print("L10")
                return False
            visited[r][c] = True    
            print("L12")
            #res= return dfs(wi+1,r+1,c) or dfs(wi+1,r,c+1) or  dfs(wi+1,r-1,c) or  dfs(wi+1,r,c-1)
            dfs(wi+1,r+1,c) or dfs(wi+1,r,c+1) or  dfs(wi+1,r-1,c) or  dfs(wi+1,r,c-1)    
            visited[r][c] = False
            return Flag
        for i in range(row):
            for j in range(col):
                if dfs(0,i,j):
                    print(i)
                    return True
        return False
 # [["C","A","A"],
 #["A","A","A"],
 # ["B","C","D"]]
        


        
                    

                    
        

        