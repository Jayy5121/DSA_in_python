
#27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        print(len(nums),nums)
        return len(nums),nums