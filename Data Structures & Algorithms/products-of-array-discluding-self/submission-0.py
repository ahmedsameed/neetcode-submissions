class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [1] * n
        prefix=1
        for i in range(1, n):
            res[i] = prefix*nums[i-1] 
            prefix=prefix*nums[i-1]
        print(res)
        postfix=1
        for i in range(n-1, -1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res


"""[1,2,4,6]
[1, 2, 8, 48]
[48,48,24,6]

[48,24,12,8]"""