class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        visited=set()
        directions=[[1,0],[0,1],[0,-1],[-1,0]]
        def dfs(i,j):
            if i<0 or j<0 or i>=ROW or j>=COL or (i,j) in visited or grid[i][j]==0:
                return 0
            
            sum=0
            visited.add((i,j))

            for dr,dc in directions:
                sum=sum+dfs(i+dr,j+dc)
            return 1+sum
        res=0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1 and (i,j) not in visited:
                    res=max(res,dfs(i,j))
        return res


        