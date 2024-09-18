import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

grp = defaultdict(list)

for i in range(N-1):
    a, b = map(int, input().split())

    grp[a].append(b)
    grp[b].append(a)

grp[0].append(1)

# print(grp)
# print(grp[1])
visited = [False]*(N+1)

lst = []

def DFS(start, visited):

    for i in grp[start]:
        if visited[i] == False:
            visited[i] = True
            if i != 1:
                lst.append((i, start))
            # print(visited)
        else:
            continue
        DFS(i, visited)
    
    return visited

DFS(0, visited)
lst.sort(key = lambda x: x[0])

for i in lst:
    print(i[1])