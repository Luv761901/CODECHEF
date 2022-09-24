T=int(input())
for i in range(0,T):
    N,X,Y=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    c=0
    for i in range(len(A)):
        a=B[i]-A[i]
        if(a==X or a==Y):
            continue
        else:
            c=1
    if(c==1):
        print("NO")
    else:
        print("YES")