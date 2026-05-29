class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap={}
        visit=set()
        for i in range(numCourses):
          premap[i]=[]
        
        for i in range(len(prerequisites)):
          premap[prerequisites[i][0]].append(prerequisites[i][1])

        def dfs(crc):
          if crc in visit:
            return False
          
          if premap[crc]==[]:
            return True

          visit.add(crc)
          for pre in premap[crc]:
            if not dfs(pre):
              return False
          visit.remove(crc)
          premap[crc]=[]
          return True
        for c in range(numCourses):
          if not dfs(c):
                return False
        return True


        
        
