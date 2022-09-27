T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    count = 0
    for i in range(N-1):
        if(S[i] == S[i+1]):
            count += 1
    res = N-count
    print(res)
