T = int(input())
for i in range(T):
    n = int(input())
    s = input()
    p = ""
    for i in s:
        if i == 'A':
            p += 'T'
        elif i == 'T':
            p += 'A'
        elif i == 'C':
            p += 'G'
        elif i == 'G':
            p += 'C'
    print(p)
