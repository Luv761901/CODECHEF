T = int(input())
for i in range(T):
    a, b, m = map(int, input().split())
    if(a > b):
        print(min(a-b, b-a+m))
    else:
        print(min(b-a, a-b+m))
