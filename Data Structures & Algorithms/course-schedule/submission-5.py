class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap=defaultdict(list)
        visit=set()
        for course,pre in prerequisites:
            premap[course].append(pre)
        def cycle(crc):
            if crc in visit:
                return False
            if premap[crc]==[]:
                return True
            visit.add(crc)
            for neigh in premap[crc]:
                if not cycle(neigh):
                    return False
            visit.remove(crc)
            premap[crc]=[]
            return True



        for i in range(numCourses):
            if not cycle(i):
                return False
        return True
        