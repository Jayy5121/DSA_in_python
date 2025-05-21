class Solution(object):
    def findErrorNums(self, nums):
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]  # [duplicate, missing]
        
        return [-1, -1]  # Shouldn't reach here for valid inputs

s1 = Solution()
print(s1.findErrorNums([1,2,2,4]))  # Correct method name