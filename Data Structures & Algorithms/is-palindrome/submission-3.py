class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            while l<r and not self.isalphaNum(s[l]):
                l=l+1

            while l<r and not self.isalphaNum(s[r]):
                r-=1  

            if s[r].lower()!=s[l].lower():
                return False

            l=l+1
            r=r-1
        return True

    def isalphaNum(self,char):
        return (ord('A')<=ord(char)<=ord('Z') 
        or ord('a')<=ord(char)<=ord('z')
        or ord('0')<=ord(char)<=ord('9'))


