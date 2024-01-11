def pel(n):
    rev=0
    temp=n
    while temp != 0:
        ld=temp %10
        rev= rev*10 +ld
        temp= temp //10
    return rev == n

num=int(input("enter number: "))

print(pel(num))