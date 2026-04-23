class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0

        minres=float("infinity")
        mapps={}
        mappt={}
        
        res=""
        #NeedMAP
        for i in range(len(t)):
            mappt[t[i]]=1+mappt.get(t[i],0)
        
        have=0
        need=len(mappt)
        #HaveMAP

        for r in range(len(s)):
            mapps[s[r]]=1+mapps.get(s[r],0)

            if s[r] in mappt and mappt[s[r]]==mapps[s[r]]:
                have+=1

            while need==have:
                
                if r-l+1<minres:
                    minres=min(minres,r-l+1)
                    res=s[l:r+1]
            
                mapps[s[l]]-=1
                if s[l] in mappt and mappt[s[l]]>mapps[s[l]]:
                    have-=1
                l=l+1
        return res if minres!=float("infinity") else ""