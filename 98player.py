a,b=map(str,input().split())
c=0
for i in a:
    if i<=b:
        c=c+1
        if c==len(a):
            print("yes")
            break
else:
    print("no")
