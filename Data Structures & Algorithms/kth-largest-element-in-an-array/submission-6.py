class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.target =len(nums)-k

        def quickselect(l,r):
            
            pivot=nums[r]
            p=l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[i],nums[p]=nums[p],nums[i]
                    p=p+1
            nums[p],nums[r]=nums[r],nums[p]
            if p>self.target:
                return quickselect(l,p-1)
            
            elif p<self.target:
                return quickselect(p+1,r)
            else:
                return nums[p]
            
        return quickselect(0,len(nums)-1)


