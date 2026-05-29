class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mappreq={}
        visit= set()

        for i in range(numCourses):
          mappreq[i]=[]

        for i in range(len(prerequisites)):
          mappreq[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(crs):
          if crs in visit:
            return False

          if mappreq[crs]==[]:
            return True
          
          visit.add(crs)
          for pre in mappreq[crs]:
            if not dfs(pre):
              return False
          visit.remove(crs)
          mappreq[crs]=[]
          return True
        for c in range(numCourses):
          if not dfs(c):
            return False
        return True

        
        