class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        maps1 = {}
        maps2 = {}

        # Frequency map of s1
        for c in s1:
            maps1[c] = 1 + maps1.get(c, 0)

        k = len(s1)  # fixed window size

        # Build the first window in s2
        for i in range(k):
            maps2[s2[i]] = 1 + maps2.get(s2[i], 0)
        if maps1 == maps2:
            return True

        # Slide the window across the rest of s2
        l = 0
        for r in range(k, len(s2)):
            # add incoming char on the right
            maps2[s2[r]] = 1 + maps2.get(s2[r], 0)
            # remove outgoing char on the left
            maps2[s2[l]] -= 1
            if maps2[s2[l]] == 0:
                del maps2[s2[l]]   # important: drop zero counts so dict comparison works
            l += 1

            if maps1 == maps2:
                return True

        return False