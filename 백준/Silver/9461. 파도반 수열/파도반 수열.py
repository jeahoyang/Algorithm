import sys

input = sys.stdin.readline

T = int(input())
lst = [1,1,1]
n =[]

for i in range(T):
    n.append(list(map(int, input().split())))
# print(n)

def DP(n):
    lst.append(lst[n-2] + lst[n-3])
    return lst

k = sorted(n)

for i in range(3, k[-1][0]):
    DP(i)

# print(lst)
for i in range(T):
    print(lst[n[i][0]-1])