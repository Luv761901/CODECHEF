T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    x = a*10
    y = b*5
    if x > y:
        print("FIRST")
    elif x < y:
        print("SECOND")
    else:
        print("ANY")
