import math
T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    a=math.ceil(x/10)
    b=math.ceil(y/10)
    print(abs(a-b))