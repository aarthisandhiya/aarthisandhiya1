a,b=map(int,input().split())
x=' '
for num in range(a+1,b):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")

player11.py
a=input()
if a=='Sunday' or a=='Saturday':
	print("yes")
elif a=='Monday'or a=='Tuesday' or a=='Wednesday' or a=='Thursday' or a=='Friday':
	print("no")



