T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    c = 0
    A.sort()
    for i in range(1, N):
        if A[i-1] == A[i]:
            c += 1
    if(c == 0 and N % 2 != 0):
        print("NO")
    else:
        print("YES")
