class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[None]*len(nums)

        for i in range(len(nums)):
            if i+k>=len(nums)-1:
                shift=i+k
                resindex=shift%len(nums)
                print(resindex)
                res[resindex]=nums[i]
                continue
            res[i+k]=nums[i]
        nums[:]=res