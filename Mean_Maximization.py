T = int(input())
P = []
b = 0
for i in range(0, T):
    N = int(input())
    x = list(map(int, input().split()))
    a = max(x)
    x.remove(a)
    b = sum(x)
    b = b/len(x)
    c = a+b
    print(c)
