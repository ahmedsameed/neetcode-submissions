class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        map={}
        for i in range(len(nums)):
            if target-nums[i] in map:
                return[map[target-nums[i]],i]
            map[nums[i]]=i
