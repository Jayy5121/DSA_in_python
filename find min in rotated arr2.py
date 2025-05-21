class Solution(object):
    def findMin(self, nums):
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]<nums[r]:
                return nums[l]
            mid=(r+l)//2
            if nums[mid]==nums[r]==nums[l]:
                l+=1
                r-=1
                continue
            if nums[mid]>nums[r]:
                l+=1
            else:
                r-=1
        return nums[l]
arr=[2,2,2,0,1]
s1=Solution()
