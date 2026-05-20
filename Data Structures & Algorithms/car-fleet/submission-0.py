class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair=[]
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        #print(pair)        
        pair.sort()
        #print(pair)
        for p,s in pair[::-1]:
           stack.append((target-p)/s)
           if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()


        return len(stack)