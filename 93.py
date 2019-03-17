a=int(input())
a=str(a)
w=0
c=0
for i in a:
    w=a.count(i)
    if w>1:
        c=c+1
        if c>0:
            print("yes")
            break
        break
else:
    print("no")
    
