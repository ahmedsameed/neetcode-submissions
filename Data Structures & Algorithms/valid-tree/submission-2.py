class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #Create adjacency list:
        adj=defaultdict(list)

        for node,neigh in edges:
            adj[node].append(neigh)
            adj[neigh].append(node)
        
        visit=set()

        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            if len(visit)==n:
                return True
            
            for neigh in adj[node]:
                if neigh==parent:
                    continue
                if not dfs(neigh,node):
                    return False
            return True
        return dfs(0,-1) and n==len(visit)