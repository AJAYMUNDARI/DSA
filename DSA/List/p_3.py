#even or odd
def sep(l,x):
    e=[]
    for i in l:
        if i<x:
            e.append(i)
    return e

l=[10, 20, 30, 40]
x=50
e=sep(l,x)
print(e)

