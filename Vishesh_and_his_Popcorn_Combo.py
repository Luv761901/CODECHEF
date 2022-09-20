T = int(input())
for i in range(0, T):
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    C1, C2 = map(int, input().split())
    a = A1+A2
    b = B1+B2
    c = C1+C2
    if(a > b and a > c):
        print(a)
    elif(b > a and b > c):
        print(b)
    else:
        print(c)
