class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visited=set()
        que=deque()

        row=len(grid)
        col=len(grid[0])
        fresh=0
        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh=fresh+1
                if grid[i][j]==2:
                    que.append([i,j])
        time=0
        while que and fresh>0:
            
            for i in range(len(que)):
                node=que.popleft()
                i,j=node
                for dr,dc in direction:
                    if i+dr>=0 and i+dr<row and j+dc>=0 and j+dc <col and grid[i+dr][j+dc]==1:

                        grid[i+dr][j+dc]=2
                        fresh=fresh-1
                        que.append([i+dr,j+dc])
            time=time+1
        return time if fresh==0 else -1




        