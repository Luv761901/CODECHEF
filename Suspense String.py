# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    s = input()
    t = []
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i] == '1':
            t.append(s[i])
        else:
            t.insert(0, s[i])
        if i < j:
            if s[j] == '1':
                t.insert(0, s[j])
            else:
                t.append(s[j])
            j -= 1
        i += 1
    print(''.join(t))
