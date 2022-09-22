T = int(input())
for i in range(0, T):
    N = int(input())
    S = ""
    X = 97
    while(len(S) < N):
        S = S+chr(X)
        X = X+1
        if(X > 122):
            X = 97
    print(S)
