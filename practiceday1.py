# practice day1
# def binarysearch(nums,target):
#     start,end=0,len(nums)-1
#     result=-1
#     while start<=end:
#         mid=(start+end)//2
#         if nums[mid]==target:
#             result=mid
#             end=mid-1
#         elif nums[mid]<target:
#             start=mid+1
#         else:
#             end=mid-1
#     return result

# # day 2
# def binarysearch(nums,target):
#     start,end=0,len(nums)-1
#     result=-1
#     while start<=end:
#         mid=(start+end)//2
#         if nums[mid]==target:
#             result=mid
#             start=mid+1
#         elif nums[mid]<target:
#             start=mid+1
#         else:
#             end=mid-1
#     return result

# def sum_inarray(nums,target):
#     start,end=0,len(nums)-1
#     while start<=end:
#         if nums[start]+nums[end]==target:
#             return [start,end]
#         elif nums[start]+nums[end]<target:
#             star+=1
#         else:
#             end=-1
#     return [-1,-1]


# def printhelllo(n):
#     if n==0:
#         return 0
#     print(n)
#     printhelllo(n-1)
# printhelllo(10)


# def febonaaci(n):
#     if n<2:
#         return n
#     return febonaaci(n-1)+febonaaci(n-2)
# print(febonaaci(50))

# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# def BS(nums,target,s,e):
#     if s>e:
#         return -1
#     mid=(s+e)//2
#     if nums[mid]==target:
#         return mid
#     elif nums[mid]<target:
#         return BS(nums,target,mid+1,e)
#     else:
#         return BS(nums,target,s,mid-1)
# nums = [1, 3, 5, 7, 9, 11]
# target = 91
# print(BS(nums, target, 0, len(nums) - 1))  

# def ceilingno(nums,target):
#     s,e=0,len(nums)-1
#     while s<=e:
#         mid=(s+e)//2
#         if nums[mid]==target:
#             return nums[mid]
#         elif nums[mid]<target:
#             s=mid+1
#         else:
#             e=mid-1
#     return nums[e]
# nums=[2,3,5,9,14,16,18]
# target=7
# print(ceilingno(nums,target))

# Binary Search in Infinite Sorted Array

# Standard Binary Search function
def binary_search(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1  # target not found

# Function to find position of target in infinite sorted array
def find_in_infinite_array(arr, target):
    start = 0
    end = 1

    # Expand the search range exponentially until target is within range
    while arr[end] < target:
        new_start = end + 1
        end = end * 2
        start = new_start

    # Now perform normal binary search in this range
    return binary_search(arr, target, start, end)

# Example Usage:
arr = [3, 5, 7, 9, 10, 13, 18, 21, 27, 30, 35, 40, 50]  # Simulating an infinite array
target = 27
print(find_in_infinite_array(arr, target))  # Output: index of 27



# #mountain array
# def Mountainarray(nums):
#     s,e=0,len(nums)-1
#     while s<e:
#         mid=(s+e)//2
#         if nums[mid]>nums[mid+1]:
#             e=mid
#         else:
#             s=mid+1
#     return nums[s]
# print(Mountainarray([0,2,1,0]))

# def findpivot(nums):
#     s,e=0,len(nums)
#     while s<=e:
#         mid=(s+e)//2
#         if mid<e and nums[mid]>nums[mid+1]:
#             return mid
#         if mid>s and nums[mid]<nums[mid-1]:
#             return mid-1
#         if nums[mid]<=nums[s]:
#             e=mid-1
#         if nums[s]<nums[mid]:
#             s=mid-1
#     return -1
# print(findpivot([3,4,5,6,7,0,1,2]))

#find pivot in with duplicate elements
# def findpivotwithduplicates(nums):
#     s,e=0,len(nums)-1
#     while s<e:
#         mid=(s+e)//2
#         if mid>s and nums[mid]>nums[mid+1]:
#             return nums[mid]
#         if mid<e and nums[mid]<nums[mid-1]:
#             return nums[mid-1]
#         if nums[mid]==nums[s] and nums[mid]==nums[e]:
#             #if pivot lies in this duplicate nums....
#             if nums[s]>nums[s+1]:
#                 return s
#             s+=1
#             if nums[e]<nums[e-1]:
#                 return e
#             e-=1
#         if nums[s]<nums[mid] or nums[s]==nums[mid] and nums[mid]>nums[e]:
#             s=mid+1
#         else:
#             e=mid-1

# print(findpivotwithduplicates([2,5,6,0,0,1,2]))


# def splitarray(nums,m):
#     start,end=0,0
#     for i in range(len(nums)):
#         start=max(start,nums[i])
#         end+=nums[i]
#     while start< end:
#         mid=(start+end)//2
#         # calculate how many picecs we can divide in 
#         sum=0
#         pieces=1
#         for num in nums:
#             if sum+num>mid:
#                 #can't add in subarray make new array
#                 sum=num
#                 pieces+=1
#             else:
#                 sum+=num
#         if pieces>m:
#             start=mid+1
#         else:
#             end=mid

#     return start
# nums=[7,2,5,8,10]
# m=2
# print(splitarray(nums,m))