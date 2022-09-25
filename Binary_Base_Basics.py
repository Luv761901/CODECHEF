T = int(input())
for i in range(0, T):
    N, K = map(int, input().split())
    S = list(input())
    count = 0
    for i in range(N//2):
        if(S[i] != S[N-1-i]):
            count += 1
    s = K-count
    if(s >= 0 and s % 2 == 0 or s >= 0 and N % 2 == 1):
        print("YES")
    else:
        print("NO")
