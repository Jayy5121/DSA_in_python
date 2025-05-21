#Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    nums.pop(j)
                else:
                    j+=1
            i+=1
        print(nums)
        return len(nums)