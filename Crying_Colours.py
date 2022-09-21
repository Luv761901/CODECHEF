T = int(input())
for i in range(0, T):
    N = int(input())
    R1, G1, B1 = map(int, input().split())
    R2, G2, B2 = map(int, input().split())
    R3, G3, B3 = map(int, input().split())
    if((R1+G2+B3)//3 == N):
        print(0)
    else:
        c1 = G1+B1+B2
        c2 = R2+R3+G3
        if(c1 > c2):
            print(c1)
        else:
            print(c2)
