import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mul = 1
cnt = 0

for i in range(N, 0, -1):
    mul *= i
    cnt += 1

    if cnt == M:
        break

a = 1
for i in range(1, M+1):
    a *= i

if M == 0:
    print(1)
else:
    print(int(mul/a))