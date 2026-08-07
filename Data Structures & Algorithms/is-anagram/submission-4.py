class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Maps={}
        Mapt={}

        if len(s)!=len(t):
            return False
        
        for char in s:
            Maps[char]=1+Maps.get(char,0)

        for char in t:
            Mapt[char]=1+Mapt.get(char,0)

        if Maps==Mapt:
            return True
        return False