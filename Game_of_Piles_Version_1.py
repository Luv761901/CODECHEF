T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if 1 in A:
        print("CHEF")

    else:
        c = 0
        for i in range(len(A)):
            if A[i] % 2 != 0:
                c += 1

        if c % 2 != 0:
            print("CHEF")
        else:
            print("CHEFINA")
