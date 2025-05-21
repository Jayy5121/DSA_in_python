class Solution(object):
    def merge(self, nums1, m, nums2, n):
        j=0
        while j<n:
            nums1[m+j]=nums2[j]
            j+=1
        nums1.sort()
        return nums1
s1=Solution()
s1.merge([1,2,3,0,0,0],3,[2,5,6],3)