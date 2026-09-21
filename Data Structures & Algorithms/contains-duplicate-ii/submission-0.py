class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapd={}
        Flag=True
        for i in range(len(nums)):
            if nums[i] in mapd:
                if i-mapd[nums[i]]<=k:
                    return True
            mapd[nums[i]]=i

        return False
                

        