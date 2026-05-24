class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        print(nums)
        res=0
        while k>0:
            res=-heapq.heappop(nums)
            k=k-1 

        return res