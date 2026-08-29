class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map={}
        r=0
        l=0
        for char in s1:
            s1Map[char]=1+s1Map.get(char,0)
        count=len(s1Map)
        print(s1Map)
        
        while r<len(s2):
            
            if s2[r] in s1Map:
                s1Map[s2[r]]=s1Map.get(s2[r],0)-1
                if s1Map[s2[r]]==0:
                    count=count-1
            
            if r-l+1>len(s1):
                if s2[l] in s1Map:
                    if s1Map[s2[l]]==0:
                        count=count+1
                    s1Map[s2[l]]=1+s1Map.get(s2[l],0)
                    
                l=l+1

            if count==0:
                return True
            r=r+1
        return False

