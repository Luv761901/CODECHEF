T = int(input())
for i in range(0, T):
    N = int(input())
    l1, l2 = [], []
    for i in range(N):
        x, y = map(int, input().split())
        l1.append(x)
        l2.append(y)
    print(len(set(l1))+len(set(l2)))
