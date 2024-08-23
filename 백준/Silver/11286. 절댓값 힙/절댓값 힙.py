import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())

lst = []
heap = []
heap_abs = []

for i in range(N):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            a = heapq.heappop(heap)
            print(a[1])

    else:
        heapq.heappush(heap, [abs(x), x])