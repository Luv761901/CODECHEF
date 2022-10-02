T = int(input())
for i in range(T):
    N = int(input())
    A = input()
    if A == A[::-1]:
        print(0)
    else:
        c = 0
        for i in range(N//2):
            if A[i] != A[N-i-1]:
                c += 1
        print((c+1)//2)
