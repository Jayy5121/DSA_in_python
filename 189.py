arr=[1,2,3,4,5]

def rotate(arr,k):
    for i in range(1,k+1):
        b=arr.pop(-1)
        arr.insert(0,b)
    return arr
print(rotate(arr,3))
    