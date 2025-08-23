class Solution(object):
    def search(self, nums, target):

        def findpivot(nums):
            start=0
            end=len(nums)-1
            while start<=end:
                mid=(start+end)//2
                if mid<end and nums[mid]>nums[mid+1]:
                    return mid
                if mid>start and nums[mid]<nums[mid-1]:
                    return mid-1
                if nums[mid]<=nums[start]:
                    end=mid-1
                else:
                    start=mid+1
            return -1

        def binaryserach(nums,target,start,end):
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return -1

        pivot=findpivot(nums)
        if pivot==-1:
            return binaryserach(nums,target,0,len(nums)-1)
        if nums[pivot]==target:
            return pivot
        if target>=nums[0]:
            return binaryserach(nums,target,0,pivot-1)
        return binaryserach(nums,target,pivot+1,len(nums)-1)

        