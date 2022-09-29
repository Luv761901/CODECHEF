for _ in range(int(input())):
    N = int(input())
    if N % 2 == 0:
        if N % 4 == 0:
            ans = 3 ^ N
        else:
            ans = 3
    else:
        if (N-1) % 4 == 0:
            ans = (3 ^ (N-1)) & N
        else:
            ans = 3
    print(ans)
