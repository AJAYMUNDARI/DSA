#average
l=[10, 20, 30, 40]
def avg():
    sum=0
    for i in l:
        sum=sum+i
    n=len(l)
    return sum/n
re=avg()
print(re)