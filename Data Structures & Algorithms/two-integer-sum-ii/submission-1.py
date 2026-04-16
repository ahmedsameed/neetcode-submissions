class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while r>l:
            sum=numbers[l]+numbers[r]
            if sum<target:
                l=l+1
                continue
            if sum>target:
                r=r-1
                continue
            if sum==target:
                return [l+1,r+1]
