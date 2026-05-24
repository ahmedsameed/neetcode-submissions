class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        minHeap=stones
        heapq.heapify(minHeap)
        while len(minHeap)>1:
            y=-heapq.heappop(minHeap)
            x=-heapq.heappop(minHeap)
            if x==y:
                continue
            if y>x:
                new=y-x
                heapq.heappush(minHeap,-new)


        if len(minHeap)==1:
            return -minHeap[0]
        return 0