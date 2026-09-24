class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapf=defaultdict(int)

        for i in range(len(nums)):
            mapf[nums[i]]+=1
            if mapf[nums[i]]>len(nums)/2:
                return nums[i]
        