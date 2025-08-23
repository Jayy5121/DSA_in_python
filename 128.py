def longestConsecative(nums):
    num_set=set(nums)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            length=1
            curr=num
            while curr+1 in num_set:
                curr+=1
                length+=1
            longest=max(longest,length)
    return longest
print(longestConsecative([100, 4, 200, 1, 3, 2]))