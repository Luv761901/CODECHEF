T = int(input())
for i in range(0, T):
    N = int(input())
    n = N
    while(N > 0):
        for i in range(1, n+1):
            print(1, end=" ")
        N -= 1
        print()
