T = int(input())
for i in range(0, T):
    T1, T2, R1, R2 = map(int, input().split())
    if((T1*T1)/(R1*R1*R1) == ((T2*T2)/(R2*R2*R2))):
        print("Yes")
    else:
        print("No")
