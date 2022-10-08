T = int(input())
for i in range(T):
    l, k = map(int, input().split())
    m = l % k
    if m == 0:
        print(0)
    else:
        print(1)
