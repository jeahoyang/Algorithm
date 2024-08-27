import sys
from collections import defaultdict

input = sys.stdin.readline

case = int(input())




for _ in range(case):
    N = int(input())
    cloth = defaultdict(list)
    lst = set()
    for i in range(N):
        N, M = map(str, input().split())
        lst.add(M)
        cloth[M].append(N)

    lst = list(lst)

    a = 1
    for i in lst:
        a = (len(cloth[i]) + 1) * a

    print(a-1)



