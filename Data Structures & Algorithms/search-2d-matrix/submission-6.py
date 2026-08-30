class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        l=0
        #matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        #target=13
        r=row-1
        while l<=r:
            mid=(l+r)//2

            if matrix[mid][0]<=target <=matrix[mid][col-1]:
                left=0
                
                right=col-1
                
                while left<=right:
                    mid2=(left+right)//2
                    if matrix[mid][mid2]==target:
                        return True
                    if matrix[mid][mid2]<target:
                        left=mid2+1
                    if matrix[mid][mid2]>target:
                        right=mid2-1
                return False
            if matrix[mid][col-1]<target :
                l=mid+1
            if matrix[mid][0]>target:
                r=mid-1
        return False 









        