class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        res=0

        for i in range(len(s)):
            l=i
            r=i

            while l>=0 and r<len(s) and (s[l]==s[r]):
                res=res+1
                l=l-1
                r=r+1
        
        for i in range(len(s)):
            l=i
            r=i+1

            while l>=0 and r<len(s) and (s[l]==s[r]):
                res=res+1
                l=l-1
                r=r+1
        return res
        
        