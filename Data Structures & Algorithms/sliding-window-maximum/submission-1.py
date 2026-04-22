class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        l=r=0
        que=collections.deque()

        while r<len(nums):
            while que and nums[que[-1]]<nums[r]:
                que.pop()
            que.append(r)

            if l>que[0]:
                que.popleft()

            if r+1>=k:
                output.append(nums[que[0]])
                l=l+1

            





            r=r+1
        return output