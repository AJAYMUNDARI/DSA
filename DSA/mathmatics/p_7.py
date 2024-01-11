def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)
a=4
b=6
print(lcm(a,b))