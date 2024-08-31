import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    R, S = map(str, input().split())
    R = int(R)

    for i in S:
        for j in range(R):
            print("".join(map(str, i)), end="")
    print()