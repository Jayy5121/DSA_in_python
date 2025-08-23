# #prime no.
# def isprime(n):
#     if n<=1:
#         return False
#     c=2
#     while c*c<=n:
#         if n%c==0:
#             return False
#         c+=1
#     return True
# for i in range(20):
#     print(i)
#     print(isprime(i))

# def sieve(n):
#     primes=[True]*(n+1)
#     primes[0]=primes[1]=False
#     for i in range(2,int(n**0.5)+1):
#         if primes[i]:
#             for j in range(i*i,n+1,i):
#                 primes[j]=False
#     for i in range(len(primes)):
#         if primes[i]:
#             print(i)
#     return primes
# print(sieve(40))

#finding out squareroot of the number
# def squareroot(n,p):
#     s,e=0,n
#     root=0.0
#     while s<=e:
#         m=(s+e)//2
#         if m*m==n:
#             return m
#         elif m*m>n:
#             e=m-1
#         else:
#             s=m+1
#     incr=0.1
#     for i in range(p):
#         while root*root<=n:
#             root+=incr
#         root-=incr
#         incr/=10
#     return root
# print(squareroot(40,3))


#Newton Raphson Method
# def NRM(n):
#     x=n
#     root=0.0
#     while True:
#         root=0.5*(x+(n/x))
#         if abs(root-x)<0.5:
#             break
#         x=root
#     return root
# print(NRM(40))

# Factors
import math

def factors(n):
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):  # start from 1
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return sorted(result)

print(factors(20))