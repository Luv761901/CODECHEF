import math
T = int(input())
for i in range(0, T):
    N = int(input())
    s = (0.143*N)**N
    d = round(s)
    print(d)
