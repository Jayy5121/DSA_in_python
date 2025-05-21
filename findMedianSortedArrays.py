class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        nums.sort()
        if len(nums)%2==0:
            leftnum=nums[:len(nums)//2]
            rightnum=nums[len(nums)//2:]
            mean=(leftnum[-1]+rightnum[0])/2.0
        else:
            mean=nums[(len(nums)-1)//2]
        print(mean)
        return mean
s1=Solution()
s1.findMedianSortedArrays([1,2],[3,4])     