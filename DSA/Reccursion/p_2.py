#recursion problem #log2 n
def fun(n):
    if n<=1:
        return 0
    else:
        return 1+fun(n//2)

fun(16)