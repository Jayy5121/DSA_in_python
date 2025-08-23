# def majorityElement(nums):
#     checked={}
#     for i,num in enumerate(nums):
#         checked[num]=checked.get(num,0)+1
#         if checked[num]>len(nums)//2:
            
#             print(checked)
#             return num
# print(majorityElement([2,2,1,1,1,2,2]))

def majorityElemnt(nums):
    count=0
    element=None
    for num in nums:
        if count==0:
            element=num
            count=1
        elif num==element:
            count+=1
        else:
            count-=1
    if nums.count(element)>len(nums)//2:
        return element
    return None
print(majorityElemnt([2,2,1,1,1,2,2]))