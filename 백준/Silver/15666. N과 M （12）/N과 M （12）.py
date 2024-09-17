import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))

lst = list(set(lst))
lst.sort()

sol = []
ans = []

def BT(start):

    if len(sol) == M:
        return print(" ".join(map(str, sol)))

    for i in range(start, len(lst)):
        sol.append(lst[i])
        BT(i)
        sol.pop()


BT(0)

