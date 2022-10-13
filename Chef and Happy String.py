# cook your dish here
T = int(input())
for i in range(T):
    s = input()
    c = f = 0
    d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for i in s:
        if i in d:
            c += 1
            if c >= 3:
                f = -1
                break
        else:
            c = 0
    if f == -1:
        print("Happy")
    else:
        print("Sad")
