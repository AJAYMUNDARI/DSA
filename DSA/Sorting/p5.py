#array union
def unionar(a,b):
    for i in range(0,len(a)):
        if i>0 and a[i-1]==a[i]:
            continue
        for j in range(0,len(b)):
            if a[i]==b[j]:
                print(a[i],end=" ")
                break
a=[10,20,15]
b=[5,17,20,30]
print(unionar(a,b))