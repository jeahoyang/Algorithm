import sys

input = sys.stdin.readline

N = int(input())

lst = [0, 1, 2, 4]
num = []

for i in range(N):
    a = int(input())

    num.append(a)

b = sorted(num)

for i in range(4, b[-1]+1):

    lst.append(lst[i-1]%1000000009 + lst[i-2]%1000000009 + lst[i-3]%1000000009)
# print(lst)
for i in num:
    print(lst[i]%1000000009)


