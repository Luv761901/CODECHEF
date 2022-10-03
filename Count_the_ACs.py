T = int(input())
for i in range(T):
    p = int(input())
    x = p//100
    y = p % 100
    if x+y <= 10:
        print(x+y)
    else:
        print(-1)
