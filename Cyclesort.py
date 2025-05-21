
class Solution(object):
    def Sort(self,num):
        i=0
        while i<len(num):
            correct_index=num[i]-1
            if num[i]!=num[correct_index]:
                num[i],num[correct_index]=num[correct_index],num[i]
            else:
                i=i+1
s1=Solution()
print(s1.Sort([2,1,4,3,6,5]))