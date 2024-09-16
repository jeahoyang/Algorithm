import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().strip())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 1:
                
                lst[nx][ny] = lst[x][y] + 1
                queue.append((nx,ny))
    
    return(lst)

print(BFS(0,0)[-1][-1])
    
    