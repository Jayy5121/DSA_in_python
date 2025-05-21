class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        op=0
        for i in range(len(nums)):
            mid=len(nums)//2
            if nums[i]>=mid:
                op=nums[i]
        return op
s1=Solution()
print(s1.majorityElement([3,3,4]))