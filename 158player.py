a,b=map(int,input().split())
c=a*b 
d=bin(c)
e=d[::-1]
for i in range(0,len(e)):
    if e[i]=="1":
        s=i
        print(i+1)
        break
