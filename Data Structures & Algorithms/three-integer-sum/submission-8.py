class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        nums.sort()
       
       
        res=set()
        for i in range(len(nums)):
            target=nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]==-target:
                   res.add((nums[l],nums[r],target))
                   
                   r-=1
                   l+=1
                
                if nums[l]+nums[r]>-target:
                   r-=1
                if nums[l]+nums[r]<-target:
                   l+=1
       
        return list(res) 
                
                
        