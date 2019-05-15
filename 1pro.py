a=input()
b=input()
result=""
maxlen=len(b) if len(a)>len(b) else  len(a)
for i in range(0,maxlen):
    if a[i]!=b[i]:
        break
    else:
        result+=a[i]
print(result)
