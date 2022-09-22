T = int(input())
for i in range(0, T):
    X, Y, Z = map(int, input().split())
    if(X >= Y and X < Z):
        print("PIZZA")
    elif(X >= Z and X < Y):
        print("BURGER")
    elif(X >= Y and X >= Z):
        print("PIZZA")
    else:
        print("NOTHING")
