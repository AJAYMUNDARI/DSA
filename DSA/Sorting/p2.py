#insertion sort
def insort(l):
    for i in range(1,len(l)):
        x=l[i]
        j=i-1
        while j>=0 and x<l[i-1]:
            l[j+1]=l[j]
            j=j-1
            l[j+1]=x

l=[10,20,40,30,50]
insort(l)
print(l)

    