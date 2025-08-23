def Pattern1(n):
    for i in range(1,n+1):
        print("*"*i)


# output
# *
# **
# ***

def Pattern2(n):
    for i in range(1,n+1):
        print("* "*n)


# output
# ***
# ***
# ***

def Pattern3(n):
    for i in range(n+1,0,-1):
        print("* "*(i-1))


# output
# * * * 
# * * 
# *



def Pattern4(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()



# output
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

def Pattern5(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

# op
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 

def pattern6(n):
    for i in range(2*n):
        col = 2*n - i if i > n else i
        for j in range (col):
            print("* ",end=" ")
        print()

print(pattern6(5))
