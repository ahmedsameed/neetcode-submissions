class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit=set()
        cycle=set()
        premap={}

        for i in range(numCourses):
            premap[i]=[]
        
        for i in range(len(prerequisites)):
            premap[prerequisites[i][0]].append(prerequisites[i][1])

        output=[]



        def dfs(i):
            if i in cycle:
                return False

            if i in visit:
                return True
            cycle.add(i)
            for nei in premap[i]:
                
                if not dfs(nei):
                    return False

            cycle.remove(i)

            visit.add(i)
            output.append(i)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
    
        