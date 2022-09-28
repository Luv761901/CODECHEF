# cook your dish here
T = int(input())
for i in range(T):
    x, y, m = map(int, input().split())
    if(x*m >= y):
        print("NO")
    else:
        print("YES")
