class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=100
        profit=0
        for i in range(len(prices)):
            if prices[i]<=minp:
                minp=prices[i]
            else:
                profit=max(profit,prices[i]-minp)
        return profit

        