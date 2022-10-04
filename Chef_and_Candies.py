import math
T = int(input())
for i in range(T):
    n, x = map(int, input().split())
    if x >= n:
        print(0)
    else:
        d = abs(n-x)
        print(math.ceil(d/4))
