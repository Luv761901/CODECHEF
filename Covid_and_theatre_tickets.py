T = int(input())
lst = []
for i in range(0, T):
    N, M = map(int, input().split())
    if N % 2 == 0:
        N = int(N/2)
    else:
        N = int(N/2)+1
    if M % 2 == 0:
        M = int(M/2)
    else:
        M = int(M/2)+1
    ans = int(M*N)
    print(ans)
