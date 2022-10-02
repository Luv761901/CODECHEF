T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    if (b-a+1) % 3 == 0:
        print("NO")
    else:
        print("YES")
