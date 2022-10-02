T = int(input())
for i in range(T):
    p, q = map(int, input().split())
    if (p+q) % 4 == 0 or (p+q-1) % 4 == 0:
        print("Alice")
    else:
        print("Bob")
