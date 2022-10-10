# cook your dish here
from collections import Counter
T=int(input())
for i in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    d=dict(Counter(A))
    m=max(d.values())
    print(len(A)-m)