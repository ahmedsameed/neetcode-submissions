class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dir=[[1,0],[-1,0],[0,-1],[0,1]]
        pacific = []
        vispacific = set()
        atlantic = []
        visatlantic= set()
        row=len(heights)
        col=len(heights[0])
        for i in range (row):
            for j in range(col):
                if i==0 or j==0:
                    pacific.append((i,j))  
                if i==row-1 or j==col-1:
                    atlantic.append((i,j)) 
        print(pacific)
        print(atlantic)

        def dfs(r,c):

            if (r,c) in vispacific:
                return 
            vispacific.add((r,c))
            for dr,dc in dir:
                print(27)
                if (r+dr) >=0 and (r+dr) <row and (c+dc)>=0 and (c+dc)<col and heights[r+dr][c+dc]>=heights[r][c]:
                    print(28)
                    pacific.append((r+dr,c+dc))
                    dfs(r+dr,c+dc)
        print(31)
        print(pacific[0])                     
        for i in range(len(pacific)):
            r,c=pacific[i]
            dfs(r,c)     
        print(33)
        print(vispacific)

        def dfs(r,c):

            if (r,c) in visatlantic:
                return 
            visatlantic.add((r,c))
            for dr,dc in dir:
                #print(27)
                if (r+dr) >=0 and (r+dr) <row and (c+dc)>=0 and (c+dc)<col and heights[r+dr][c+dc]>=heights[r][c]:
                    #print(28)
                    atlantic.append((r+dr,c+dc))
                    dfs(r+dr,c+dc)
        print(49)
        #print(pacific[0])                     
        for i in range(len(atlantic)):
            r,c=atlantic[i]
            dfs(r,c)     
        print(54)
        print(visatlantic)

        res=[]
        for i in range (row):
            for j in range (col):
                if (i,j) in vispacific and (i,j) in visatlantic:
                    res.append([i,j])
        return (res)



        