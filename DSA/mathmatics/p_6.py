def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

c=10
d=3
print(gcd(c,d))