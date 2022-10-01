p1, p2, p3, p4 = map(int, input().split())
c = 0
if p1 >= 10:
    c += 1
if p2 >= 10:
    c += 1
if p3 >= 10:
    c += 1
if p4 >= 10:
    c += 1
print(c)
