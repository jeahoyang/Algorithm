import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[0]*(N+1)]
xy = []

for _ in range(N):
    lst.append([0] + list(map(int, input().split())))

for _ in range(M):
    xy.append(list(map(int, input().split())))

# print(lst)
# print(xy)


# for i in xy:
#     sol = 0
#     for j in range(i[0]-1, i[2]):
#         sol += sum(lst[j][i[1]-1 : i[3]])
#     print(sol)

for i in range(1, N+1):
    for j in range(1, N+1):
        lst[i][j] += lst[i-1][j] + lst[i][j-1] - lst[i-1][j-1]

# print(lst)

for i in xy:
    x1, y1, x2, y2 = i
    sol = lst[x2][y2] - lst[x1-1][y2] - lst[x2][y1-1] + lst[x1-1][y1-1]
    print(sol)