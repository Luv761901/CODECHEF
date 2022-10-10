# cook your dish here
import math
from collections import Counter
T = int(input())
for i in range(T):
    x = int(input())
    A = list(map(int, input().split()))
    d = dict(Counter(A))
    m = max(d.values())
    print(math.ceil(math.log(m, 2)))
