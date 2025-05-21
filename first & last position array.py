class Solution(object):
    def searchRange(self, nums, target):
        def findfirst(nums,target):
            l,r=0,len(nums)-1
            f=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    f=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return f
        def findlast(nums,target):
            l,r=0,len(nums)-1
            last=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    last=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return last
        first=findfirst(nums,target)
        last=findlast(nums,target)
        return [first,last]
s1=Solution()
print(s1.searchRange([5,7,7,8,8,10],8))
