T = int(input())
for i in range(T):
    p = input()
    a, b, temp = [1], [0], p[0]
    mod = 998244353
    loop = p[1:]
    for i in loop:
        if i == temp:
            m = a[-1]
            a.append(m+b[-1])
            b.append(0)
        else:
            m = a[-1]
            a.append(m+b[-1])
            b.append(m)
        temp = i
    print((a[-1]+b[-1]) % mod)
