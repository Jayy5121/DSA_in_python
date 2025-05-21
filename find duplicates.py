class Solution(object):
    def findDuplicate(self, nums):
        i=0
        while i<len(nums):
            if nums[i]!=i+1:
                correct=nums[i]-1
                if nums[i]!=nums[correct]:
                    nums[i],nums[correct]=nums[correct],nums[i]
                else:
                    return nums[i]
            else:
                i+=1
s1=Solution()
print(s1.findDuplicate([2,1,4,2,6,5]))