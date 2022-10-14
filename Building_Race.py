# cook your dish here
T=int(input())
for i in range(T):
    a,b,x,y=map(int,input().split())
    m=a/x
    n=b/y
    if m==n:
        print("Both")
    elif m<n:
        print("Chef")
    else:
        print("Chefina")