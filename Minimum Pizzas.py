# cook your dish here
import math
T = int(input())
for i in range(T):
    n, t = map(int, input().split())
    x = n*t
    print(math.ceil(x/4))
