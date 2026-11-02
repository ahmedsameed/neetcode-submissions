class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmaps1={}
        hashmaps2={}
        for char in s1:
            hashmaps1[char]=1+hashmaps1.get(char,0)
        l=0
        r=0
        while r<len(s2):
            hashmaps2[s2[r]]=1+hashmaps2.get(s2[r],0)

            while r-l+1>len(s1):
                
                hashmaps2[s2[l]]-=1
                if hashmaps2[s2[l]]==0:
                    del hashmaps2[s2[l]]

                l=l+1
                print(r-l+1)
                
            
            print(hashmaps2)
            if hashmaps1==hashmaps2:
                return True

            r=r+1
        return False
        