import sys

input = sys.stdin.readline

N = int(input())

lst = [0, 3, 7, 17]


for i in range(4, N+1):
    lst.append(2*lst[i-1]%9901 + lst[i-2]%9901)

print(lst[N]%9901)


