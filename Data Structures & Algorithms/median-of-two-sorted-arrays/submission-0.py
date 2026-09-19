class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A=nums1
        B=nums2

        half=(len(nums1)+len(nums2))//2

        if len(nums1)>len(nums2):
            A,B=B,A

        l=0
        r=len(A)-1

        while True:
            i=(l+r)//2
            j=half-i-2
            print(j)
            Aleft=A[i] if i>=0 else float("-infinity")
            Aright=A[i+1] if i+1<len(A) else float("infinity")
            Bleft=B[j] if j>=0 else float("-infinity")
            Bright=B[j+1] if j+1<len(B) else float("infinity")
            print(Bright)

            if Aleft<=Bright and Aright >= Bleft:
                if (len(nums1)+len(nums2))%2:
                    return min(Aright,Bright)
                return (min(Aright,Bright)+max(Aleft,Bleft))/2
            
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1
        



        