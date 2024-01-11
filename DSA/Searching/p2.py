#Recursive binary seacring
def bsearch(l,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if l[mid]==x:
        return mid
    elif l[mid]>x:
        bsearch(l, low, mid-1)
    else:
        bsearch(l, mid+1, high)
        

l=[10,20,30,40,50,60]
x=70
low=0
high=len(l)-1
a=bsearch()
print(a)