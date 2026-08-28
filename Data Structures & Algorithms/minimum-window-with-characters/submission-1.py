class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Okay so we run a window over the array. Soon as we have all the chars for our substring, we store the result and size. Then we hunt for the best. How? Shorten the array moving the left pointer. As soon we are in 'deficit', we more the right pointer till we have all chars. if this substring is shorter than our last result we update and move the left pointer again. We do this till we reach the end of the right pointer."""
        if t=="":
            return ""
        count={}
        window={}
        l=0
        resLen=float("infinity")
        res=[-1,-1]
        for c in t:
            count[c]=1+count.get(c,0)
        have=0
        need=len(count)
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in count and window[c] and count[c]==window[c] :
                have=have+1

            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1

                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have=have-1
                l=l+1

        

        return s[res[0]:res[1]+1] if resLen !=float("infinity") else ""
