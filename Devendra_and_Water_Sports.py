T = int(input())
for i in range(0, T):
    Z, Y, A, B, C = list(map(int, input().split()))
    a = Z-Y
    b = A+B+C
    if(a >= b):
        print("YES")
    else:
        print("NO")
