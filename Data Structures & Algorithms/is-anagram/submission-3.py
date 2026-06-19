class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        maps={}
        mapt={}

        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]]=1
            else:
                maps[s[i]]=1+maps[s[i]]
        for i in range(len(t)):
            if t[i] not in mapt:
                mapt[t[i]]=1
            else:
                mapt[t[i]]=1+mapt[t[i]]

        
        if mapt==maps:
            return True
        return False

            
        