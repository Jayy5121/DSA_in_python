# def check(nums):
#     def pivot(nums):
#         s,e=0,len(nums)-1
#         while s<=e:
#             mid=(s+e)//2
#             if nums[mid]==nums[s] and nums[mid]==nums[e]:
#                 s+=1
#                 e-=1
#                 continue
#             if mid<e and nums[mid]>nums[mid+1]:
#                 return mid
#             if mid>s and nums[mid]<nums[mid-1]:
#                 return mid-1
#             if nums[mid]<=nums[s]:
#                 e=mid-1
#             else:
#                 s=mid+1
#         return -1
#     print(pivot(nums))
#     n=pivot(nums)
#     if n==-1:
#         return True
#     return nums[n+1:] + nums[:n+1] == sorted(nums)
# print(check([2,6,1,3,4,5,7]))
class Solution(object):
    def check(self, nums):
        count_breaks = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  
                count_breaks += 1
            if count_breaks > 1:
                return False
        
        return True
obj = Solution()
print(obj.check([1,1,1,1]))        

