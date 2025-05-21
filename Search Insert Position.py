class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
s1=Solution()
s1.searchInsert([1,3,5,6],5)
    
        