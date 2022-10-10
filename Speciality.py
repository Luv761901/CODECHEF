# cook your dish here
T = int(input())
for i in range(T):
    x, y, z = map(int, input().split())
    if x > y and x > z:
        print("Setter")
    elif y > z and y > x:
        print("Tester")
    else:
        print("Editorialist")
