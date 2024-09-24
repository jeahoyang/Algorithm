import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for i in range(1,N+1):
    queue.append(i)


i = 1
while True:

    if len(queue) == 1:
        break
    
    if i%2 == 1:
        queue.popleft()
        i += 1
        # print(queue)
    else:
        a = queue.popleft()
        queue.append(a)
        i += 1


print(queue[0])