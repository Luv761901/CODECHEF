T = int(input())
for i in range(0, T):
    N, X = map(int, input().split())
    a = list(map(int, input().split()))
    s, count = 0, 0
    if(sum(a) < X):
        print(-1)
    else:
        a.sort()
        a.reverse()
        if(sum(a) < X):
            print(-1)
        elif(sum(a) == X):
            print(N)
        else:
            for i in a:
                if(s < X):
                    s = s+i
                    count += 1
                else:
                    break
            print(count)
