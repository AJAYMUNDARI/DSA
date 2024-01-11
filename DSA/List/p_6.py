#reverse a list
def revl(l):
    i=0
    e=len(l)-1
    while i<e:
        l[i],l[e]=l[e],l[i]
        i=i+1
        e=e-1
l=[10,20,30]
revl(l)
print(revl(l))
    