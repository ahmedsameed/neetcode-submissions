class Solution:
    def isValid(self, s: str) -> bool:
        
        mapd={")":"(",'}':'{',"]":"["}
        stack=[]
        for i in range(len(s)):
            
            if s[i] in mapd and stack:
                print("9")
                print(s[i])
                #s[i]==> ]
                print("12")
                print(stack[-1])
                print("L12")
                print(s[i])
                print(mapd[s[i]])
                if mapd[s[i]]==stack[-1]:
                    print("10")
                    stack.pop()
                else:
                    return False
        
            else:
                print(16)
                stack.append(s[i])
                print(stack)

        if stack:
            return False
        return True


        
        
        
        
        
        """for loop
        traverse array
        if current element is )
            check if stack.pop is (
        else 
        add to stack"""
        