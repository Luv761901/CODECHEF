T = int(input())
for i in range(0, T):
    K = int(input())
    c = 0
    while(K % 2 == 0):
        K = K//2
        c += 1
    print(c)
