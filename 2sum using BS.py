class Solution(object):
    def twoSum(self, numbers, target):
        l,r=0,len(numbers)-1
        while l<r:
            current_sum=numbers[l]+numbers[r]
            if current_sum==target:
                return [l+1,r+1]
            elif current_sum>target:
                r-=1
            else:
                l+=1

    def twoSum2(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
