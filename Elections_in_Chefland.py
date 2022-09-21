T = int(input())
for i in range(0, T):
    XA, XB, XC = map(int, input().split())
    if(XA > 50):
        print("A")
    elif(XB > 50):
        print("B")
    elif(XC > 50):
        print("C")
    else:
        print("NOTA")
