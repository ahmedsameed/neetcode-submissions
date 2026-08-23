class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        heap=[]
        for x,y in points:
            dist=((x*x))+((y*y))
            heap.append([dist,x,y])
        heapq.heapify(heap)

        while k>0:
            dist,x,y=heapq.heappop(heap)
            res.append([x,y])
            k=k-1
        return res




        