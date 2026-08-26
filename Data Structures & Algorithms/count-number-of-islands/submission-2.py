class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        visited=set()

        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        def dfs(i,j):
            if (i,j) in visited or i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
                return
            visited.add((i,j))
            for dr,dc in direction:
                dfs(i+dr,j+dc)
            
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visited :
                    dfs(i,j)
                    res=res+1

        return res