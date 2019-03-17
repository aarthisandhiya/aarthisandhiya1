a=int(input())
r=[int(a) for a in input().split()]
i=2
c=0
if int(r[0])%i==0:
    for d in r:
        if d%i==0:
            c=c+1 
        else:
            print(d)
else:
    for w in r:
        if w%i==1:
            c=c+1 
        else:
            print(w)
            
    
