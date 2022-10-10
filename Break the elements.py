# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    o, e = 0, 0
    for i in A:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    if o == len(A) or e == len(A):
        print(0)
    else:
        print(e)
