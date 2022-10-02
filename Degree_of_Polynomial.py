T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    s=0
    i=1
    while(i!=N):
        if A[N-i]!=0:
            s+=N-i
            break
        else:
            i+=1
    print(s)    