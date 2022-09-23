T=int(input())
for i in range(0,T):
    X,Y,Z=map(int,input().split())
    a=X*Y
    b=X*Z
    print(b-a)