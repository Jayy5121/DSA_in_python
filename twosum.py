class Solution(object):
    def twoSum(self, nums, target):
        output=[]
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                if nums[i] + nums[j]== target:
                    output.append(i)
                    output.append(j)
        print(output)
        return output
s1=Solution()
s1.twoSum([4,5,2,7,1,8,3,2,3],9)