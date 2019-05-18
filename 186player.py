a=input().split()
a=list(a)
c=0
d=0
for i in a:
    if i=="Vishal":
        c=c+1
    elif i=="Sundar":
        d=d+1
if c>0 and d>0:
    print("yes")
else:
    print("no")
