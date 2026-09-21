class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups=set()
        l=0

        for r in range(len(nums)):
            if r-l>k:
                dups.remove(nums[l])
                l=l+1
            if nums[r] in dups:
                return True
            dups.add(nums[r])

        return False

                

        