T = int(input())
for i in range(T):
    N = int(input())
    n1, n2, n3, n4 = map(int, input().split())
    a = [n1, n2, n3, n4]
    print(max(a))
