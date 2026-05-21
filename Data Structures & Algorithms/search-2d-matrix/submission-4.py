class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        column=len(matrix[0])
        top=0
        bottom=len(matrix)-1
        while top<=bottom:
            mid=(top+bottom)//2
            #print(mid)
            if target>matrix[mid][-1]:
                top=mid+1
            elif target<matrix[mid][0]:
                bottom=mid-1
            else:
                break

        print(mid)
        start=0
        end=column-1
        while start<=end:
            
            center=(start+end)//2
            print(matrix[mid][center])
            if target>matrix[mid][center]:
                start=center+1
            if target<matrix[mid][center]:
                end=center-1
            if target==matrix[mid][center]:
                
                return True
        if start>end:
            return False



            
