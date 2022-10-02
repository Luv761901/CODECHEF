import math
T = int(input())
for i in range(T):
    n, x = map(int, input().split())
    if n < 6:
        print(x)
    else:
        a = math.ceil(n/6)
        print(a*x)
