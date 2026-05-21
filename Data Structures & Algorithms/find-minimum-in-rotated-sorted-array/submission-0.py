class Solution:
    def findMin(self, nums: List[int]) -> int:
        inf=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                inf=i
        return nums[inf]
        