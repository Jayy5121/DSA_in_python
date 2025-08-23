# def evenodd(num):
#     return num&1 == 1;

# print(evenodd(25)) # true=odd else even

# def XOR(nums):
#     unique=0
#     for i in range (len(nums)):
#         unique^=nums[i]
#     return unique
# print(XOR([2,1,1,2,4]))

# def magicno(n):
#     ans=0
#     base=5
#     while n>0:
#         last=n&1
#         n=n>>1
#         ans+=last*base
#         base=base*5
#     return ans

# print(magicno(5))
# from math import log
# n = 10
# b = 16
# ans = int(log(n, b)) + 1
# print(ans)       

# def power1(base,power):
#     ans=1
#     while power>0:
#         if (power & 1)==1:
#             ans*=base
#         base*=base
#         power=power>>1
#     return ans
# print(power1(2,2))

def setbit(n):
    count=0
    while n>0:
        n=(n&(n-1))
        count+=1
    return count
print(setbit(10))