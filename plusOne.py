class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1         
                return digits
        digits.insert(0,1)
        return digits
s1=Solution()
digits=[1,2,3] 
digits=s1.plusOne(digits)
print(digits)