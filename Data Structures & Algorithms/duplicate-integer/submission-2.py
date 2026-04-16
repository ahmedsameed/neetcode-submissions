class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """HASHMAP"""
        dict={}
        for i in range(0,len(nums)):
            if nums[i] in dict:
                return True
            else: 
                dict[nums[i]]=i
        return False





        