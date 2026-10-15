class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        l=0
        count=defaultdict(int)
        for r in range(len(s)):
            while count[s[r]]>0:
                count[s[l]]-=1
                l=l+1
                
            maxlen=max(maxlen,r-l+1)
            count[s[r]]+=1
        return maxlen