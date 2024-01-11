#check the list is sorted or not
def checksort(l):
    for item in l:
        i=1
        if (l[i]>l[i+1]):
            return False
        i=i+1
    return True
l=[10, 30, 29,40]
res=checksort(l)
print(res)