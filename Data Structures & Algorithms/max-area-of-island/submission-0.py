class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        visited = set()

        def bfs(i, j):
            area = 1
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            que = deque()
            que.append((i, j))
            while que:
                i, j = que.popleft()
                for rd, cd in direction:
                    r, c = i+rd, j+cd
                    if (r, c) not in visited and r>=0 and c>=0 and r<row and c<column and grid[r][c] == 1:
                        visited.add((r, c))
                        area += 1
                        que.append((r, c))
            return area

        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    count = max(count, bfs(i, j))
        return count
