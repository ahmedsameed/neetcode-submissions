class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        maps1 = {}
        maps2 = {}

   
        for c in s1:
            maps1[c] = 1 + maps1.get(c, 0)

        k = len(s1)  
        
        for r in range(len(s2)):
            # add the incoming char
            maps2[s2[r]] = 1 + maps2.get(s2[r], 0)

            # once the window is bigger than k, shrink from the left
            if r >= k:
                l = r - k
                maps2[s2[l]] -= 1
                if maps2[s2[l]] == 0:
                    del maps2[s2[l]]

            # now the window is exactly size k whenever r >= k - 1
            if r >= k - 1 and maps1 == maps2:
                return True

        return False