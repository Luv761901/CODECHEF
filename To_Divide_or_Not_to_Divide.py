T = int(input())
for i in range(T):
    a, b, n = map(int, input().split())
    if a % b == 0:
        print(-1)
    else:
        if n % a == 0:
            c = n//a
            if n % b == 0:
                c += 1
            print(c*a)
        else:
            c = (n//a)+1
            if((c*a) % b == 0):
                c += 1
            print(c*a)
