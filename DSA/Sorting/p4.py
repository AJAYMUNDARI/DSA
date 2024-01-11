#array union
def unionar(a,b):
    c=a+b
    c.sort()
    for i in range(0,len(c)):
        if(i==0 or c[i]!=c[i-1]):
            print(c[i],end=" ")
a=[10,20,15]
b=[5,17,20,30]
l=unionar(a,b)
print(l)