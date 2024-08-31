import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lst = deque()

for i in range(N):
    a = int(input())
    

    if a == 0:
        lst.pop()
    else:
        lst.append(a)


print(sum(lst))