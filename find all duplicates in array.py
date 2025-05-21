class Solution(object):
    def findDuplicates(self, nums):
        i=0
        op=[]
        while i<len(nums):
            correct=nums[i]-1
            if nums[i]!=nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                op.append(nums[i])
        return op
s1=Solution()
print(s1.findDuplicates([4,3,2,7,8,2,3,1]))