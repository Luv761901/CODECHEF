T=int(input())
for i in range(T):
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    B=A[:]
    B.sort()
    if A==B:
        print("YES")
    else:
        f=0
        for i in range(n-1):
            if(A[i]>A[i+1]):
                if A[i]+A[i+1]<=x:
                    temp=A[i]
                    A[i]=A[i+1]
                    A[i+1]=temp
                else:
                    f=-1
                    break
        if f!=-1:
            print("YES")
        else:
            print("NO")