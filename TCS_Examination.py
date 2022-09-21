T = int(input())
for i in range(0, T):
    DSA, TOC, DM = map(int, input().split())
    DSA1, TOC1, DM1 = map(int, input().split())
    a = DSA+TOC+DM
    b = DSA1+TOC1+DM1
    if(a > b):
        print("DRAGON")
    elif(b > a):
        print("SLOTH")
    else:
        if(a == b):
            if(DSA > DSA1):
                print("DRAGON")
            elif(DSA1 > DSA):
                print("SLOTH")
            else:
                if(a == b):
                    if(DSA == DSA1):
                        if(TOC > TOC1):
                            print("DRAGON")
                        elif(TOC1 > TOC):
                            print("SLOTH")
                        else:
                            print("TIE")
