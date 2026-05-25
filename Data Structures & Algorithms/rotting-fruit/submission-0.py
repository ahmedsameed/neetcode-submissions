class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

      row=len(grid)
      column=len(grid[0])
      time=0
      fresh=0
      queue=deque()
      for i in range(row):
        for j in range(column):
          if grid[i][j]==1:
            fresh=fresh+1
          if grid[i][j]==2:
            queue.append([i,j])
      direction=[[0,1],[-1,0],[0,-1],[1,0]]
      while queue and fresh >0:
        for i in range(len(queue)):
          i,j=queue.popleft()
          for dr,dc in direction:
            row=i+dr
            column=j+dc
            if(row<0 or row==len(grid) or column<0 or column==len(grid[0]) or grid[row][column]!=1):
              continue
            grid[row][column]=2
            queue.append([row,column])
            fresh=fresh-1
        time=time+1

      return time if fresh==0 else  -1
