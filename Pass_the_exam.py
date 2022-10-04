T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    if a >= 10 and b >= 10 and c >= 10:
        if (a+b+c) >= 100:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")
