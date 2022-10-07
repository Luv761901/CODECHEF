for i in range(int(input())):
    n = int(input())
    if n < 2:
        print(0)
    else:
        if n % 2 == 0:
            ans = 2*(n//2)*(n//2)
        else:
            ans = 2*(n//2)*(n//2+1)
        print(ans)
