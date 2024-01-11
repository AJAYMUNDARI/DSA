x=int(input("enter num:"))
res=0
while x>0:
    x=x//10
    res=res+1
print("no of digits: ",res)