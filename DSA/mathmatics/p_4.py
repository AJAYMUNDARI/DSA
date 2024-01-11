def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)

num=int(input("enter num: "))
print(fac(num))