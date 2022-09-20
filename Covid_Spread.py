T = int(input())
for i in range(0, T):
    ans = 1
    N, D = map(int, input().split())
    for i in range(0, D):
        if(i < 10):
            ans = ans*2
        else:
            ans = ans*3
        if(ans >= N):
            ans = N
            break
    print(ans)
