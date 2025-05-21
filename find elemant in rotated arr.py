class Solution(object):
    def search(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[l]==nums[r]:
                l+=1
                r-=1
                continue
            if nums[l]<=nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r-=1
                else:
                    l+=1
            else:
                if nums[mid]< target<= nums[r]:
                    l=mid+1
                else:
                    r-=1
        return False
s1=Solution()
print(s1.search([2,5,6,0,0,1,2],3))