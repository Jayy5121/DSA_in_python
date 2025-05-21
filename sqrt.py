class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        l,r=1,x
        result=1
        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                result=mid
                l=mid+1  
            else:
                r=mid-1
        return result
        