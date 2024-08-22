import sys

input = sys.stdin.readline

N = int(input())
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))

# print(lst)

lst.sort()

# print(lst)

for i in range(N):
    print(" ".join(map(str, lst[i])))