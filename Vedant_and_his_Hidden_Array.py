T = int(input())
for i in range(0, T):
    N, A = map(int, input().split())
    if(N == 1):
        if(A % 2 == 0):
            print("EVEN")
        else:
            print("ODD")
    else:
        if(A % 2 == 0):
            print("IMPOSSIBLE")
        else:
            if(N % 2 == 0):
                print("EVEN")
            else:
                print("ODD")
