class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in range(0,len(nums)):
            if nums[i] in dict:
                print("L6")
                return True
            else: 
                dict[nums[i]]=i
                print(dict[nums[i]])
        return False





        