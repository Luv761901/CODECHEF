# cook your dish here
import math
T = int(input())
for i in range(T):
    n = int(input())
    S = input()
    m = 0
    for i in range(len(S)):
        if S[i] != '0':
            m += 1
        else:
            break
    print(m)
