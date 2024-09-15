import sys

input = sys.stdin.readline

N = int(input())

lst = []

for i in range(N):
    R, G, B = map(int, input().split())
    lst.append([R,G,B])

for i in range(N):
    for j in range(3):
        if i == 0:
            pass
        else: 
            lst[i][j] += min(lst[i-1][j-1], lst[i-1][j-2])
    
print(min(lst[N-1]))