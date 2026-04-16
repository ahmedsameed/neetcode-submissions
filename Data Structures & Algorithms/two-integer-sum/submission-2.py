class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range (0,len(nums)):
            dict[nums[i]]=i
            
        print(dict)
        for i in range (0,len(nums)):
            if target - nums[i] in dict :
                if dict[target - nums[i]] != i: 
                    return [i,dict[target - nums[i]]]