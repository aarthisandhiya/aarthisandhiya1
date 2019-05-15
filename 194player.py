a,b=map(str,input().split())
if a=='S'and b=='P':
    print('S')
elif a=='S'and b=='R':
    print("R")
elif a=='P' and b=='S':
    print("S")
elif a=='P' and b=='R':
    print("P")
elif a=='R' and b=='P':
    print("P")
elif a=='R' and b=='S':
    print("R")
elif a=='S' and b=='S':
    print("D")
elif a=='P' and b=='P':
    print("D")
elif a=='R' and b=='R':
    print("D")
