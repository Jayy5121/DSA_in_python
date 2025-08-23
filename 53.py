def maxsubarray(nums):
    sum,maxi=0,0
    start=-1
    for i in range(len(nums)):
        if sum==0:
            start=i
        sum+=nums[i]
        if sum>maxi:
            maxi=sum
            ansStart=start
            ansEnd=i
        if sum<0:
            sum=0
    return nums[ansStart:ansEnd]
print(maxsubarray([-2,-3,4,-1,-2,1,5,-3]))