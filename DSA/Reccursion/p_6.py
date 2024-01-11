def fun(n):
    if n<10:
        return 
    return fun(n//10)+n%10

fun(38)