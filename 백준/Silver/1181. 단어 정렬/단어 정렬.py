import sys

input = sys.stdin.readline

N = int(input())
lst = []

for i in range(N):
    lst.append(input().strip())

# print(lst)

lst = list(set(list(lst)))

lst.sort()
lst.sort(key=len)



for i in lst:
    print(i)
