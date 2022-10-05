T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if y <= x:
        print(y)
    else:
        print(x)
