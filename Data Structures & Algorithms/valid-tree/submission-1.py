class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True


        mapn={}

        for i in range(n):
            mapn[i]=[]
        
        for i in range(len(edges)):
            mapn[edges[i][0]].append(edges[i][1])
            mapn[edges[i][1]].append(edges[i][0])

        visit=set()

        def dfs(node,prev):
            if node in visit:
                return False
            
            visit.add(node)

            for j in mapn[node]:
                if j==prev:
                    continue
                if not dfs(j,node):
                    return False
            return True
        return dfs(0,-1) and n==len(visit)
        