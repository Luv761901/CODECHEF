T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if x < y:
        print(0)
    else:
        print(x-y)
