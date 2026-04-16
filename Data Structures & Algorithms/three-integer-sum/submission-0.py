class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res=[]
        map={}
        for i in range (len(nums)):
            map[nums[i]]=1+map.get(nums[i], 0)
        print(map)

        for i in range(len(nums)):
            map[nums[i]]=map[nums[i]]-1
            if i and nums[i]==nums[i-1]:
                print("Ahmed")
                continue

            for j in range(i+1,len(nums)):
                
                map[nums[j]]=map[nums[j]]-1    
                if j-1>i and nums[j]==nums[j-1]:
                    continue
                sum=-1*(nums[i]+nums[j])
                if sum in map and map[sum]>0:
                    print(i)
                    print(j)
                    res.append([nums[i],nums[j],sum])
            for j in range(i+1,len(nums)):
                map[nums[j]]=map[nums[j]]+1
            
                
        return res

        