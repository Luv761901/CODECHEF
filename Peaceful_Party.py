T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    s=a+c
    if(s>b):
        print(s)
    else:
        print(b)