class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        r=0
        count={}

        while r<len(s):
            count[s[r]]= 1+count.get(s[r],0)
            
            
            if r-l+1 -max(count.values())>k:
                count[s[l]]= count.get(s[l],0)-1
                l=l+1
            res=max(res,r-l+1)
            r=r+1
        return res

        
                



        