class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack=[]
        maxarea=0
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1]>heights[i]:
                index,val=stack.pop()
                maxarea=max(maxarea,(i-index)*val)
                print("L11")
                print(maxarea)
                start=index
            stack.append([start,heights[i]])

        for index,val in stack:
            
            maxarea=max(maxarea,(len(heights)-index)*val)
            print("l19")
            print(maxarea)
        return maxarea