import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()

result = []
# sol = []

def BT():

    if len(result) == M:
        print(" ".join(map(str, result)))
        # sol.append(result[0])
        return

    for i in lst:
        if i in result:
            pass
        else:
            result.append(i)
            # print(result)
            BT()
            result.pop()

BT()
# print(sol)

