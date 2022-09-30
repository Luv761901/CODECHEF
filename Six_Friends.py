T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    s = 3*x
    p = 2*y
    print(min(s, p))
