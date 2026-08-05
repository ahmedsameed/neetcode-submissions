class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp={}

        def dfs(i,amount):
            if (i,amount) in dp:
                return dp[(i,amount)]
            if amount==0:
                return 1
            
            if i>=len(coins):
                return 0
            
            if amount >= coins[i]:
                dp[(i,amount)]=dfs(i+1,amount)+dfs(i,amount-coins[i])
                
            else:
                dp[(i,amount)]=dfs(i+1,amount)
            return dp[(i,amount)]
        return dfs(0,amount)            


        