T = int(input())
for i in range(T):
    n = int(input())
    b = []
    p = n
    j = 1
    f = 0
    for i in range(n):
        if f == 0:
            b.append(p)
            p -= 1
            f = 1
        else:
            b.append(j)
            j += 1
            f = 0
    b = b[::-1]
    for i in b:
        print(i, end=" ")
    print()
