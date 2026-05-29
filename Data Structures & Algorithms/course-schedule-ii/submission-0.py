class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      premap={}
      for i in range(numCourses):
        premap[i]=[]

      for i in range(len(prerequisites)):
        premap[prerequisites[i][0]].append(prerequisites[i][1])

      output=[]
      visit=set()
      cycle=set()

      def dfs(crc):
        if crc in cycle:
          return False
        if crc in visit:
          return True
        
        cycle.add(crc)
        for pre in premap[crc]:
          if not dfs(pre):
            return False
        cycle.remove(crc)
        visit.add(crc)
        output.append(crc)
        return True
      
      for c in range(numCourses):
        if dfs(c)==False:
          return []
      return output
        
         

        