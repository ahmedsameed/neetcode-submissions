class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}

        for cnt in tasks:
            count[cnt]=1+count.get(cnt,0)

        maxHeap=[-c for c in count.values()]

        heapq.heapify(maxHeap)

        q=deque()
        time=0
        while q or maxHeap:
            time+=1
            
            if not maxHeap:
                time=q[0][1]


            else:
                cont=1+heapq.heappop(maxHeap)
                if cont:
                    q.append([cont,time+n])

            if q and time==q[0][1]:
                heapq.heappush(maxHeap,q.popleft()[0])
            
        return time

        