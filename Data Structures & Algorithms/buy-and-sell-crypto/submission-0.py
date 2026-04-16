class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        maxsum=0
        sum=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                sum=prices[j]-prices[i]
                maxsum=max(sum,maxsum)

        if maxsum<0:
            return 0
        return maxsum

