import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []


def BT(x):

    # print(lst)
    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return
        

    for i in range(x, N+1):
        lst.append(i)
        BT(i)
        lst.pop()

BT(1)


