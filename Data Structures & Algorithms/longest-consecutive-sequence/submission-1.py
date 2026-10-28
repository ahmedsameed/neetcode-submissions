class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset=set()

        for num in nums:
            numset.add(num)
        res=0
        for num in nums:
            if num-1 not in numset:
                length=0
                while num in numset:
                    length+=1
                    num=num+1
                res=max(res,length)
             
        return res