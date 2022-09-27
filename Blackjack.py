T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    dif=21-(a+b)
    flag=0
    for i in range(1,11):
        if(dif==i):
            flag+=1
            break
    if(flag==0):
        print(-1)
    else:
        print(dif)