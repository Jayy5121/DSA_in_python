def maxConsecative(nums):
    count=0
    maxi=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            count=0
        maxi=max(maxi,count)
    return maxi
print(maxConsecative([1,1,0,1,1,1]))