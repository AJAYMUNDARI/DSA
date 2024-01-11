#even or odd


def sep(l):
    e=[]
    o=[]
    for i in l:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    return e,o
l=[10, 20, 30, 40]
e=sep(l)
o=sep(l)
print(e)
print(o)
