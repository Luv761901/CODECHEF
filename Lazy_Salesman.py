T = int(input())
for i in range(T):
    n, w = map(int, input().split())
    A = list(map(int, input().split()))
    sum1 = 0
    while(sum1 < w):
        sum1 += max(A)
        A.remove(max(A))
    print(len(A))
