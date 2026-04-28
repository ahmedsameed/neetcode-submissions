class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        deq=deque()
        output=[]
        #in the deque, we dont store nums[i], we store i
        l=0
        r=0
        while r<len(nums):
            while deq and nums[r]>nums[deq[-1]] :
                deq.pop()
                
            deq.append(r)

            #what happends our current max is out of current window
            
            if l>deq[0]:
                deq.popleft()

            if r+1>=k:
                output.append(nums[deq[0]])
                l=l+1

            r=r+1

        return output
