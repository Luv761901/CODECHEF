T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    c = 0
    d = abs(b-a)
    for i in range(1, int(d**0.5)+1):
        if d % i == 0:
            if d//i == i:
                c += 1
            else:
                c += 2
    print(c)
