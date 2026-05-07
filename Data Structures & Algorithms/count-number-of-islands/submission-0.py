class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        column=len(grid[0])
        island=0
        visited=set()

        def bfs (i,j):
            
            que=deque()
            que.append((i,j))
            while que:
                i,j = que.popleft()
                direction=[[1,0],[-1,0],[0,1],[0,-1]]    
                for rd, cd in direction:
                    print(i+rd)
                    print(j+cd)
                    if  (i+rd,j+cd) not in visited and i+rd>=0 and j+cd>=0 and i+rd<row and j+cd<column and grid[i+rd][j+cd] =="1" :
                       # print(i)
                        #print(j)
                        visited.add((i+rd,j+cd))
                        que.append((i+rd,j+cd))


        for i in range(row):
            for j in range(column):
                if grid[i][j]=="1" and (i,j) not in visited:
                    
                    bfs (i,j)
                    #print(island) 
                    island=island+1
                
        return island
        