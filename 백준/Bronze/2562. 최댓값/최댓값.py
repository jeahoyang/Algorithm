import sys

input = sys.stdin.readline


lst = []

for i in range(9):
    lst.append(list(map(int, input().split()))[0])

a = sorted(lst)

print(a[-1])
print(lst.index(a[-1])+1)