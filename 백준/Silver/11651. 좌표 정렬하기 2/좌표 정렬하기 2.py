import sys

input = sys.stdin.readline

N = int(input())

lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort()
lst.sort(key= lambda x:x[1])

for i in range(N):
    print(" ".join(map(str, lst[i])))