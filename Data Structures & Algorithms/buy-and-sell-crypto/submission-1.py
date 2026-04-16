class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        profit =0 
        minbuy=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<minbuy:
                minbuy=prices[i]
            
            profit=prices[i]-minbuy

            maxprofit=max(maxprofit,profit)
        
        return maxprofit

