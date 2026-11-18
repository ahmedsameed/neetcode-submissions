class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def radix(nums,base):
            if not nums:
                return nums
            exp=1

            while max(nums)//exp>0:
                buckets=[[] for i in range(base)]

                for num in nums:
                    digit=(num//exp)%base
                    buckets[digit].append(num)
                #new_nums=[]

                nums=[n for bucket in buckets for n in bucket]

                exp*=base
            return nums
        negative=[-num for num in nums if num<0 ]#[-5,-25-,-6,-19], [5 25 6 19]
        positive=[num for num in nums if num>=0 ]
        postivesorted=radix(positive,10)
        negativesorted= reversed(radix(negative,10))# [-25 -19 -6 -5]
        negativesortedor= [-n for n in negativesorted]
        return negativesortedor+postivesorted


        
        