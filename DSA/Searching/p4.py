#insex of last occurance
def indunc(l,x):
    low=0
    high= len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]<x:
            low=mid+1
        elif l[mid]>x:
            high=mid-1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1
    return -1

l=[10,20,30,40,40,50,60]
x=40
ar=indunc(l,x)
print(ar)