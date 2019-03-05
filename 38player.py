d=int(input())
x=' '
for i in range(1,d+1):
    if d%i==0 and i%2==0:
        x=x+str(int(i))+' '
print(x.strip())
