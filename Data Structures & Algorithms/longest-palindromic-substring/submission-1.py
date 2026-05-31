class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx=0
        resLen=0
        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>resLen:
                    residx=left
                    resLen=right-left+1
                left=left-1
                right=right+1

            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>resLen:
                    residx=left
                    resLen=right-left+1
                left=left-1
                right=right+1
        return s[residx:residx+resLen]





                



        