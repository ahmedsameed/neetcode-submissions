class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        res=0
        visit=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i,j):
            if (i,j) in visit:
                return 0

            visit.add((i,j))
            res=0
            for dr,dc in directions:
                nr=i+dr
                nc=j+dc

                if nr<0 or nc<0 or nr>=row or nc>=col or (nr,nc) in visit or grid[nr][nc]==0:
                    continue
                
                res=res+dfs(nr,nc)

            return 1+res

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    print("27")
                    res=max(res,dfs(i,j))

        return res


        