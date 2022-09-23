T = int(input())
for i in range(0, T):
    N, K, X = map(int, input().split())
    n = 0
    if(K < X):
        print(-1)
    else:
        A = []
        while(len(A) < N):
            A.append(n)
            n = (n+1) % X
        for i in A:
            print(i, end=" ")
    print("")
