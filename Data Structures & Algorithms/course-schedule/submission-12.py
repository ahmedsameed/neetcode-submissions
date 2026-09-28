class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjmap=defaultdict(list)

        for course,pre in prerequisites:
            adjmap[course].append(pre)

        #Now we will check the eligility for every course from 0 to         numcouses-1
        
        ##[[0,1],[1,2][2,3][3,1]]
        #numCourses=2
        #prerequisites=[[0,1],[1,0]]
        
        # 1: None 4
        # 2 :None 4
        #3 :1 2
        #[[0,1],[1,0]]
        
        #0 :1
        #1: 0
        visit=set()
        def dfs(i):    
            if i in visit:
                return False
            
            #print(visit)
            if adjmap[i]==[]:
                return True
            visit.add(i)
            
            for nei in adjmap[i]: 
                if not dfs(nei):
                    return False
            visit.remove(i)
            
            adjmap[i]=[] 
            return True


        for i in range(numCourses):
            
            if not dfs(i):
                return False
        return True

        

