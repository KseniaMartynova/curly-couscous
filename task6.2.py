a=int(input())
b=int(input())
x=0
y=0
def gcd(a,b):
    if a==0:
        return b,0,1
    gdc,x1,y1=gcd(b%a,a)
    x=y1-(b//a)*x1
    y=x1
    return gdc,x,y
print(gcd(a,b))
#chek
q,w,e=gcd(a,b)
if a*w+b*e==q:
    print('TRue')
