class Solution:
    def isValid(self, s: str) -> bool:
        mapd={')':'(','}':'{',']':'['}
        if not s:
            return True
        stack=[]
        for i in range(len(s)):
            if s[i] in mapd and stack:
                if not mapd[s[i]]==stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
         
        if not stack:
            return True
        return False

        
        