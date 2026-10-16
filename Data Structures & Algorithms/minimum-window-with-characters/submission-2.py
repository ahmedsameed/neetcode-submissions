class Solution:
    def minWindow(self, s: str, t: str) -> str:
        Tdic={}

        for char in t:
            Tdic[char]=1+Tdic.get(char,0)
        
        Sdic=defaultdict(int)
        r=0
        l=0
        res=[]
        reslen=float('inf')
        have=0
        need=len(Tdic)
        while r<len(s):
            Sdic[s[r]]+=1
            if s[r] in Tdic and Sdic[s[r]]==Tdic[s[r]]:
                have+=1
            while have==need:
                if r-l+1<reslen:
                    reslen=r-l+1
                    res=s[l:r+1]
                Sdic[s[l]]-=1
                if s[l] in Tdic and Tdic[s[l]]> Sdic[s[l]]:
                    have-=1
                l=l+1
            r=r+1
        return ''.join(res)
                            
             
