T = int(input())
for i in range(T):
    a, b, x = map(int, input().split())
    if (b-a) % (x*2) == 0:
        print("YES")
    else:
        print("NO")
