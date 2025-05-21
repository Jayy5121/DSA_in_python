class MountainArray(object):
    def get(self, index):
        pass
    def length(self):
        pass
class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        
        def findpeak(mountainArr):
            l,r=0,mountainArr.length()-1
            while l<r:
                mid=(l+r)//2
                if mountainArr.get(mid)>mountainArr.get(mid+1):
                    r=mid
                else:
                    l=mid+1
            return l
        def findtarget(mountainArr,target,start,end,ascending=True):
            while start<=end:
                mid=(start+end)//2
                mid_val=mountainArr.get(mid)

                if mid_val==target:
                    return mid
                
                if ascending:
                    if mid_val<target:
                        start=mid+1
                    else:
                        end=mid-1
                else:
                    if mid_val<target:
                        end=mid-1
                    else:
                        start=mid+1
            return -1
        
        peak=findpeak(mountainArr)
        op=findtarget(mountainArr,target,0,peak,ascending=True)
        if op!=-1:
            return op
        return findtarget(mountainArr,target,peak+1,mountainArr.length()-1,ascending=False)
