import sys

input = sys.stdin.readline

S = input().strip().split('-')
lst = []

for i in S:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)

    lst.append(cnt)

a = lst[0]
b= 0

for i in lst[1:]:
    b += i

print(a-b)
