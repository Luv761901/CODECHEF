T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    if a+b<c:
        print("YES")
    elif b+c<a:
        print("YES")
    elif c+a<b:
        print("YES")
    else:
        print("NO")