class Solution(object):
    def firstMissingPositive(self, nums):
        i=0
        while i<len(nums):
            correct=nums[i]-1
            if nums[i]>0 & nums[i]!=nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)
        
s1 = Solution()
print(s1.firstMissingPositive([3,4,-1,1]))