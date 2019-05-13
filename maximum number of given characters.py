ASCII_SIZE=256
def maximum(data):
    count=[0]*ASCII_SIZE
    max=-1
    c=''
    for i in data:
        count[ord(i)]=count[ord(i)+1]
    for i in data:
        if max<count[ord(i)]:
            max=count[ord(i)]
        c=i 
    return c
data=input()
a=maximum(data)
print(a)           
