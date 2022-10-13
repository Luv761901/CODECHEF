# cook your dish here
import math
T = int(input())
for i in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    max1, max2 = -math.inf, -math.inf
    c1, c2 = 0, 0
    for i in range(len(A)):
        c1 += A[i]
        max1 = max(max1, c1)
    for i in range(len(A)-1, -1, -1):
        c2 += A[i]
        max2 = max(max2, c2)
    m = max(max1, max2)
    for i in range(len(B)):
        if B[i] > 0:
            m += B[i]
    print(m)
