import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())

    G[u].append(v)
    G[v].append(u)
    G[u].sort()
    G[v].sort()

# print(G)

visited = [False]*(N)

def DFS(start, visited):
    visited[start-1] = True
    for v in G[start]:
        if visited[v-1] == False:
            DFS(v, visited)

    return visited

# print(DFS([1][0], visited))

i = 1
check = 1

while False in visited:

    if False in DFS([i][0], visited):
        DFS([i][0], visited)
        # print(visited)
        i = DFS([i][0], visited).index(False)+1
        check += 1
    else:
        break

print(check)
