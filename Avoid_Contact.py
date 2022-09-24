T = int(input())
for i in range(0, T):
    X, Y = map(int, input().split())
    if(X != Y):
        a = X-Y
        b = Y*2
        print(a+b)
    else:
        print((Y*2)-1)
