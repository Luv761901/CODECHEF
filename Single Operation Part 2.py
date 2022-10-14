# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    S = input()
    a = []
    for i in S:
        if i == '0':
            a.append(i)
        elif i == '1' and i not in a:
            a.append(i)
        else:
            break
    print(len(a))
