class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows =len(grid)
        cols=len(grid[0])
        visit=set()
        q=deque()
        def addcell(row,col,d):
            if row<0 or col<0 or row==rows or col==cols or (row,col) in visit or grid[row][col]==-1:
                return
            visit.add((row,col))
            grid[row][col]=d
            q.append([row,col])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    q.append([row,col])
                    visit.add((row,col))
        
        
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                d=grid[row][col]+1
                addcell(row+1,col,d)
                addcell(row,col+1,d)
                addcell(row-1,col,d)
                addcell(row,col-1,d)
            

        



        