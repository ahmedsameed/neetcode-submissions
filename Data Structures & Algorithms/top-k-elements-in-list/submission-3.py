class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=0
                dict[num]=dict[num]+1
            else:
                dict[num]=dict[num]+1
        
        heap=[]
        for num in dict.keys():
            heapq.heappush(heap,(dict[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        for num in heap:
            print(num)
            res.append(num[1])
        return res

        
        """dict={}
        for num in nums:
            if num  not in dict:
                dict[num]=0
                dict[num]=dict[num]+1
            else: 
                dict[num]=dict[num]+1

        arr=[]
        for num,cnt in dict.items():
            arr.append([cnt,num])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res"""
        
        
        