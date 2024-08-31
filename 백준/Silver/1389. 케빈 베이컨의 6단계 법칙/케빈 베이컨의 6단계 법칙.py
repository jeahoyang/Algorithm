import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lst = defaultdict(list)
que = deque()

for i in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)
    lst[x].sort()
    lst[y].sort()




def BFS(start ):
    # print(visited), 
    visited = [0]*(N+1)
    que.append(start)
    visited[start] = 1
    while que:

        v = que.popleft()
        # print(v)
        # print(que)

        # if visited[v] == 0:
        #     # print(cnt)

        for i in lst[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1

                que.append(i)


    return sum(visited)



# print(BFS(1))
# print(BFS(2))
# print(BFS(3))
# print(BFS(4))
# print(BFS(5))


b = []

for i in range(1, N+1):
    a = BFS(i)
    # print(i, a)
    b.append((i,a))

# print(b)
b.sort(key= lambda x:x[1])
print(b[0][0])


