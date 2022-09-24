T=int(input())
for i in range(0,T):
    P=int(input())
    if(P%2==0):
        a=(P//2)+1
        print(a)
    else:
        a=(P//2)
        b=P%2
        print(a+b)