T = int(input())
for i in range(T):
    N = int(input())
    if N <= 3:
        print(-1)
    elif N == 4:
        print(3, 1, 4, 2)
    else:
        i = 1
        while(i <= N):
            print(i, end=" ")
            i += 2
        j = 2
        while(j <= N):
            print(j, end=" ")
            j += 2
