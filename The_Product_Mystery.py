import math
T = int(input())
for i in range(T):
    b, c = map(int, input().split())
    m = math.gcd(b, c)
    print(c//m)
