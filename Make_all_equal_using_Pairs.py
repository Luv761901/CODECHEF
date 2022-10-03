T = int(input())
for i in range(T):
    n = int(input())
    A = list(input().split())
    d = {}
    for i in A:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    s = sorted(d.values())
    m = max(s)
    print(n-m)
