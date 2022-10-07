T = int(input())
for i in range(T):
    n = int(input())
    A = []
    for i in range(n):
        temp = list(map(int, input().split()))
        A.append(temp[1:])
    x = [1, 2, 3, 4, 5]
    f = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if list(set(A[i]+A[j])) == x:
                f = 1
            if f == 1:
                break
        if f == 1:
            break
    if f == 1:
        print("YES")
    else:
        print("NO")
