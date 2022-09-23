T = int(input())
for i in range(0, T):
    A, B, C = map(int, input().split())
    if(A+B == C or B+C == A or C+A == B):
        print("YES")
    else:
        print("NO")
