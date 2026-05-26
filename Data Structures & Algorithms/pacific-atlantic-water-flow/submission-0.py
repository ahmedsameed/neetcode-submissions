class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row=len(heights)
        column=len(heights[0])
        pac=set()
        atl=set()

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or r<0 or r==row or c<0 or c==column or heights[r][c]<prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        for i in range(row):
            dfs(i,0,pac,heights[i][0])
            dfs(i,column-1,atl,heights[i][column-1])
        
        for i in range(column):
            dfs(0,i,pac,heights[0][i])
            dfs(row-1,i,atl,heights[row-1][i])
        res=[]
        for i in range(row):
            for j in range(column):
                if (i,j) in pac and (i,j) in atl:
                    res.append((i,j))
        return res

        