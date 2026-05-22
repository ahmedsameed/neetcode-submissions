class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        flag=[False] *n
        subset=[] 
        def dfs():
            if len(subset)==n:
                res.append(subset.copy())
                return
            for i in range(len(nums)): #0
                if flag[i]==True:
                    continue
                subset.append(nums[i])     
                flag[i]=True
                dfs()                                                   
                subset.pop()
                flag[i]=False
                
        dfs()
        return res
        


                
        