class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COLS=len(grid[0])
        visited=set()
        maxarea=0
        directions=[[0,1],[-1,0],[0,-1],[1,0]]
        def dfs(i,j):
            if i>=ROW or i<0 or j>=COLS or j<0 or grid[i][j]==0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            sum=0
            for dr,dc in directions:
                sum=sum+dfs(i+dr,j+dc)
            return 1+sum 
        for i in range (ROW):
            for j in range(COLS):
                if grid[i][j]==1 and (i,j) not in visited:
                    
                    maxarea=max(maxarea,dfs(i,j))
        return maxarea
        



        