T = int(input())
for i in range(T):
    x, p, q = list(map(int, input().split()))
    print(x*(p-q))
