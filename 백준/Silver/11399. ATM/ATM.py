import sys

input = sys.stdin.readline

N = int(input())


lst = list(map(int, input().split()))

lst.sort()
sum = 0

for i in range(1, N+1):
    sum = sum + i*lst[-i]
    # print(sum)

print(sum)
