T = int(input())
for i in range(0, T):
    S = input()
    n = len(S)
    if(n < 2):
        print("NO")
    else:
        c = 0
        for i in range(0, n-1):
            if(S[i] == '1' and (S[i+1] == '0' or S[i+1] == '1')):
                c += 1
                break
        if(c == 1):
            print("YES")
        else:
            print("NO")
