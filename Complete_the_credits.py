# cook your dish here
T = int(input())
for i in range(0, T):
    X = int(input())
    if(X > 65):
        print("Overload")
    elif(X < 35):
        print("Underload")
    else:
        print("normal")
