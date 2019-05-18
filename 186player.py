a=input().split()
a=list(a)
c=0
d=0
e=0
for i in a:
    if i=="Vishal":
        c=c+1
    elif i=="Sundar":
        d=d+1
    elif i=="VishalSundar" or i=="SundarVishal" or i=="Vishal_Sundar" or i=="Sundar_Vishal":
        e=e+1
if c>0 and d>0 or e>0:
    print("yes")
else:
    print("no")
    
    
