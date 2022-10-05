T = int(input())
for i in range(T):
    x, y, n, r = map(int, input().split())
    if((r//y) >= n):
        print(0, n)
    elif (r//x) < n:
        print(-1)
    else:
        p = y*n
        q = x-y
        s = (r-p)//q
        if ((r-(p)) % q != 0):
            s += 1
        print(s, (n-s))
