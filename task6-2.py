def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input())
if prost(a):
    print('True')
else:
    print('FAlse')
#проверка
for n in range(2,a):
    if a%n==0:
        print('Clognoe')
        break
        
    
                

        

