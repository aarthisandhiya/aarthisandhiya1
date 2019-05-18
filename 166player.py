a,b=map(int,input().split())
f=1 
i=1
while a>0:
    f=f*a
    a=a-1

w=1
while b>0:
    w=w*b 
    b=b-1
    
def hcf(f,w):
    if( w==0):
        return f 
    else:
        return hcf(w,f%w)
        
c=hcf(f,w)
print(c)
