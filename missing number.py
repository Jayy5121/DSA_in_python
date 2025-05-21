class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        count=0
        for i in range(len(nums)):
            if nums[i]==i:
                count+=1
            else:
                return i
        return count
