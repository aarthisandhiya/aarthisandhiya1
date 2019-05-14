def fact(num):
    factorial=1 
    if num>0:
        for i in range(1,num+1):
            factorial=factorial*i 
    
    return factorial

num1,num2=map(int,input().split())
s=fact(num1)
k=fact(num2)
r=s//k
print(r)


