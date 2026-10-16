class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i=0  
        j=len(nums)-1
        if k>len(nums):
            k=k%len(nums)
        def reverse(left,right):
            while left<right:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                left=left+1
                right=right-1
        reverse(i,j)
        reverse(i,k-1)
        reverse(k,j)



