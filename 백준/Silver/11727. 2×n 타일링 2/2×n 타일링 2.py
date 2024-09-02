import sys

input = sys.stdin.readline

N = int(input())

lst = [0, 1]

for i in range(2, N+1):
    if i%2 == 0:
        lst.append(lst[i-1]*2+1)
    else:
        lst.append(lst[i-1]*2-1)

print(lst[N]%10007)

