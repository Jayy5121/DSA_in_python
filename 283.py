# brute force
# def move_zeroes(nums):
#     for i in range(len(nums)):
#         for j in range(i,(len(nums))):
#             if nums[i]==0:
#                 nums[j],nums[i]=nums[i],nums[j]
#     return nums
# print(move_zeroes([1, 3, 12, 0, 0,5,15,8,0,4,8,0,4,5,6,7,0,0,4,5]))


#optimal soln
def moveZeroes(nums):
    j=-1
    for i in range(len(nums)):
        if nums[i]==0:
            j=i
            break
    if j==-1:
        return nums
    for i in range(j,len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
    return nums
print(moveZeroes([1, 3, 12, 0, 0,5,15,8,0,4,8,0,4,5,6,7,0,0,4,5]))