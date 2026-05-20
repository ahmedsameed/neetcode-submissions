class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums, start, end):
            if start > end:        # base case
                return -1
            
            mid = (start + end) // 2
            
            if target < nums[mid]:
                return binary(nums, start, mid - 1)
            elif target > nums[mid]:
                return binary(nums, mid + 1, end)
            else:
                return mid
        
        return binary(nums, 0, len(nums) - 1)