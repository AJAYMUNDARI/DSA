def zer(n):
    i=5
    rev=0
    while (i<=n):
        res=res+n//i
        i=i*5
    return res
num=int(input("enter number "))
print(zer(num))