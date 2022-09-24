T = int(input())
for i in range(0, T):
    A, B, C, P, Q, R = map(int, input().split())
    avg = (P+Q+R)/2
    sum = A+B+C
    if(sum > avg):
        print("YES")
    else:
        a = max(P-A, Q-B, R-C)
        sum = sum+a
        if(sum > avg):
            print("YES")
        else:
            print("NO")
