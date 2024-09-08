import sys

input = sys.stdin.readline

N = int(input())
G = []
visited = [0 for _ in range(N)]

for i in range(N):
    G.append(list(map(int, input().split())))  

def DFS(x):
    for i in range(N):
        if G[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            # print(visited)
            DFS(i)
            # print(visited)


visited = [0 for _ in range(N)]

for i in range(N):
    DFS(i)
    print(" ".join(map(str, visited)))
    visited = [0 for _ in range(N)]