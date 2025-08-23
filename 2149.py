def rearrangeArray(nums):
    positivenum,negitivenum=[],[]
    for num in nums:
        if num <0:
            negitivenum.append(num)
        else:
            positivenum.append(num)
    op=[]
    for i in range(len(positivenum)):
        op.append(positivenum[i])
        op.append(negitivenum[i])
    return op
print(rearrangeArray([3,1,-2,-5,2,-4]))