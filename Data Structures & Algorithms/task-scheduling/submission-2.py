class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mapd={}
        for i in range(len(tasks)):
            if tasks[i] in mapd:
                mapd[tasks[i]]=mapd[tasks[i]]+1
            else:
                mapd[tasks[i]]=1

        maxHeap=[]
        k = list(mapd.values()) 
        print(k)
        for i in range(len(k)):
            maxHeap.append(-k[i])
        print(maxHeap)
        heapq.heapify(maxHeap)   # ← THIS IS MISSING — must heapify before popping!

        time=0
        que=deque()
        while que or maxHeap:
            time=time+1
            if maxHeap:
                cur=1+heapq.heappop(maxHeap)
                if cur:
                    que.append([cur,time+n])
        
            if que and que[0][1]==time:
                heapq.heappush(maxHeap,que.popleft()[0])
        return time


