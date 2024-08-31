import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
G = defaultdict(list)

for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

a = deque()

def BFS(start):
    visited = [0]*(N+1)
    visited[start] = 1
    a.append(start)

    

    while a:
        
        v = deque.popleft(a)

        for i in G[v]:
            if visited[i] == 0:
                visited[i] = 1
                a.append(i)

    return sum(visited)

print(BFS(1) -1)



