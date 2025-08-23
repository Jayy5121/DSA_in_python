def subarraysum(nums,k):
    count=0
    # for i in range(len(nums)):
    #     sum=0
    #     for j in range(i,len(nums)):
            
    #         sum=sum+nums[j]
    #         if sum==k:
    #             count+=1
    # return count
    sum=0
    mp={0:1}
    
    for i in range(len(nums)):
        sum+=nums[i]
        remove=sum-k
        count+=mp.get(remove,0)
        mp[sum]=mp.get(sum,0)+1
    return count
print(subarraysum([1,1,1],2))