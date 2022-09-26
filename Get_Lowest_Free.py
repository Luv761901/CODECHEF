T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    A = []
    A.append(a)
    A.append(b)
    A.append(c)
    m = min(A)
    A.remove(m)
    print(sum(A))
