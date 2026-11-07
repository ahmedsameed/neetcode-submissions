class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i,n in enumerate(asteroids):
            while stack and stack[-1]>0 and n<0 :
                if abs(n)>abs(stack[-1]):
                    stack.pop()
                elif abs(n)<abs(stack[-1]):
                    n=0
                else:
                    n=0
                    stack.pop()
            if n!=0:
                stack.append(n)
            


            
        return stack
            

            
        