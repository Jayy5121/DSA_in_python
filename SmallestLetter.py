class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l,r=0,len(letters)-1
        while l<=r:
            mid=(l+r)//2
            if letters[mid]<=target:
                l=mid+1
            else:
                r=mid-1
        return letters[l%len(letters)]
        