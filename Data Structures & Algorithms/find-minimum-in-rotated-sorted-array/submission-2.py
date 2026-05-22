class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        minres=nums[left]
        while left<=right:
            if nums[left]<=nums[right]:
                minres=min(minres,nums[left])
                break

            mid=(left+right)//2
            minres=min(minres,nums[mid])

            if nums[mid]>=nums[left]:
                left=mid+1
            else:
                right=mid-1
        return minres