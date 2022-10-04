import math
T = int(input())
for i in range(T):
    mt, mn, sn = map(int, input().split())
    s = math.ceil(sn/mn)
    ans = 0
    if s <= mt:
        while(s != 0):
            if mn > sn:
                mn = sn
            ans += mn**2
            sn = sn-mn
            s -= 1
        print(ans)
    else:
        while(mt != 0):
            ans += mn**2
            mt -= 1
        print(ans)
