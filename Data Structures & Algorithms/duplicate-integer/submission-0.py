class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        qa=0;
        for i in range(0,len(nums)):
            if my_dict.get(nums[i]) is None:  
                my_dict[nums[i]] = i
            else:     
                qa=qa+1    
        if qa==0: 
            return False
        else: 
            return True





        