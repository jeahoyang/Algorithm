import sys

input = sys.stdin.readline

N = int(input())
lst_N = set(map(int, input().split()))
M = int(input())
lst_M = list(map(int, input().split()))


# print(lst_N)
for i in lst_M:
    if i in lst_N:
        print(1)
    else:
        print(0)