T = int(input())
for i in range(T):
    n, x = map(int, input().split())
    m = n-x
    if m < x:
        print(m)
    else:
        print(x)
