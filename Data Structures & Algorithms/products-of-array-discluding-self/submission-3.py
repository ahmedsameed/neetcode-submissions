class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixarray=[1]*(len(nums))
        suffixarray=[1]*len(nums)

        curpro=1
        
        for i in range(0,len(nums)):
            prefixarray[i]=curpro
            curpro=curpro*nums[i]

        curpro=1
         
        for i in range(len(nums)-1,-1,-1):
            suffixarray[i]=curpro
            curpro=curpro*nums[i]
        #print(suffixarray)

        for i in range(len(nums)):
            prefixarray[i]=prefixarray[i]*suffixarray[i]

        return prefixarray
            
