#merge list
def merge(a,b):
    res=[]
    n=len(a)
    m=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i=i+1
        else:
            res.append(b[j])
            j=j+1
    while i<m:
        res.append(a[i])
        i=i+1
    while j<n:
        res.append(b[j])
        j=j+1
return res
a=[10,50]
b=[5,15,30,60]
ar=merge(a,b)
print(ar)
    
