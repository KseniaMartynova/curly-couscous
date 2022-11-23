a=int(input())
b=int(input())
c=0
maxi=0
if a==0:
    print(b)
if a>0 and b>0:
    for c in range(1,b+1):
        if a%c==0 and b%c==0:
            if c>maxi:
                maxi=c
print(maxi)

#Проверка
g=a//maxi
k=b//maxi
p=0
proverka=0
if g>0 and k>0:
    for p in range(1,k+1):
        if g%p==0 and k%p==0:
            if p>proverka:
                proverka=p
    if proverka==1:
        print('pravilno')
    else:
        print('nepravilno')
                

