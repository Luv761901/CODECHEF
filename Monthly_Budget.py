# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    s=Y*30
    if(s<=X):
        print("YES")
    else:
        print("NO")