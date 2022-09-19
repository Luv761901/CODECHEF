T = int(input())
for i in range(0, T):
    N, x, y = map(int, input().split())
    if((x+y) % 2 == 0):
        print(0)
    else:
        print(1)
