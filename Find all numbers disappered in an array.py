class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        count=0
        op=[]
        for i in range(1,len(nums)):
            if nums[i]==i:
                count+=1
            else:
                op.append(i)
            return op
        return [count]
s1=Solution()
print(s1.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
