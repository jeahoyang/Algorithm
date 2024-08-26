import sys
import heapq

input = sys.stdin.readline

N = int(input())
lst = []


for i in range(N):
    x = list(map(int, input().split()))
    # print(x)
    heapq.heappush(lst, -x[0])
    if len(lst) == 0:
        print(0)
        break
    else:
        if x[0] == 0:
            # print(lst)
            a = heapq.heappop(lst)
            
            print(-a)

