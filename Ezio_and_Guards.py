T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    if(a>=b):
        print("YES")
    else:
        print("NO")