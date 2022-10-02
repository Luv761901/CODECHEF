T = int(input())
for i in range(T):
    x, n = map(int, input().split())
    if x == 1:
        print(0)
    else:
        print((x-1)*(2*n-x))
