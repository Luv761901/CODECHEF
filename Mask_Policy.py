T = int(input())
for i in range(0, T):
    N, A = map(int, input().split())
    X = N-A
    if(A == X):
        print(A)
    elif(X > A):
        print(A)
    elif(X < A):
        print(X)
