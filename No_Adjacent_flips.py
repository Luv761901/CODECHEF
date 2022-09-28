for _ in range(int(input())):
    N = int(input())
    arr = []
    ans = 0
    S = input()
    for i in range(N):
        if S[i] == '1':
            arr.append(i)
    if len(arr) == 0:
        print(0)
    else:
        flag = 0
        for i in arr:
            if (i+1) in arr or (i-1) in arr:
                print(2)
                flag = 1
                break
        if flag == 0:
            print(1)
