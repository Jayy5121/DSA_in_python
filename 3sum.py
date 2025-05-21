class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        target=0
        s=set()
        op=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum<target:
                    j+=1
                else:
                    k-=1
        op=list(s)
        return op