class Solution(object):
    def numberOfSteps(self, num):
        
        def helper(num,count):
            if num==0:
                return count
            else:
                if num%2==0:
                    return helper(num//2,count+1)
                else:
                    return helper(num-1,count+1)
        return helper(num,0)
s1=Solution()
print(s1.numberOfSteps(14))