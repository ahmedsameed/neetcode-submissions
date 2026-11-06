class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank=[1]*n
        par=[i for i in range(n)]
        def find(n1):
            if n1!=par[n1]:
                par[n1]=find(par[n1])
            return par[n1]

        
        def union(n1,n2):
            par1=find(n1)
            par2=find(n2)
            if par1==par2:
                return 0
            
            if rank[par2]>rank[par1]:
                par1,par2=par2,par1
            rank[par1]+=rank[par2]
            par[par2]=par1
            return 1



        for n1,n2 in edges:
            n-=union(n1,n2)

        return n

            
        