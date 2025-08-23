

def pascaltringle(n):
    ans=[]
    for i in range(0,n):
        ans.append(ncr(i+1))
    return ans
def ncr(row):
    ans=1
    ansrow=[1]
    for i in range(1,row):
        ans=ans*(row-i)//i
        ansrow.append(ans)
    return ansrow
print(pascaltringle(5))


