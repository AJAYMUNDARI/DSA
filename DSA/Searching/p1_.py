#binary seacring
def bsearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low=mid+1
        else:
            high=high-1
    return -1

l=[10,20,30,40,50,60]
x=70
a=bsearch(l,x)
print(a)