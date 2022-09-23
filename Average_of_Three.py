T = int(input())
for i in range(0, T):
    X = int(input())
    a = 3*X
    b = int(a/2)
    c = int(a % 2)
    d = int(b+c)
    for i in range(1, d+1):
        for j in range(i+1, d+1):
            for k in range(j+1, d+1):
                if(i+j+k == a):
                    print(i, j, k)
                else:
                    break
                break
            break
