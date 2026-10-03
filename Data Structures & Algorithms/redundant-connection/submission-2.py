class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        """setlen=set()

        for n1,n2 in edges:
            setlen.add(n1)
            setlen.add(n2)"""

        n=len(edges)
        
        
        """Initially treat every node as a seperate componenet

        Union of two edges

        If we find redundant connection between nodes 1, 2 via an edge ie par(1)==par(2):
        return (edge(1,2))
        """
        par=[i for i in range(0,n+1)]
        print(par)
        rank=[1]*(n+1)

        def find(node):
            print(node)
            if node==par[node]:
                return node
            return find(par[node])

        def union (n1,n2):
            p1=find(n1)
            p2=find(n2)
        
            if p1==p2:
                return False

            if rank[p2]>rank[p1]:   #p1 is always big
                p1,p2=p2,p1
            par[p2]=p1
            rank[p1]=rank[p1]+rank[p2]
            return True

        
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

        

        