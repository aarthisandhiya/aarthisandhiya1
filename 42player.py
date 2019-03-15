
a=int(input())
test_list=[str(a) for a in input().split()]
flag = 0
i = 1
while i < len(test_list)-1: 
    if(test_list[i] <= test_list[i+1]): 
        flag = 1
        break
    i += 1
if flag>0:
    print("yes")
elif flag==0: 
    print ("No")
