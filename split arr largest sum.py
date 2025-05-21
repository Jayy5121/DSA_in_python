class Solution(object):
    def splitArray(self, nums, k):
        start,end=0,0
        for i in range(len(nums)):
            start=max(start,nums[i])
            end+=nums[i]

        while start<end:
            mid =(start+end)//2
            sum=0
            pieces=1
            for i in nums:
                if sum+i>mid:
                    sum=i
                    pieces+=1
                else:
                    sum+=i
            if pieces > k:
                start=mid+1
            else:
                end=mid
        return start
        