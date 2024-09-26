import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = []

for i in range(1, N+1):
    lst.append(i)


i = 0
sol = []
while len(lst) > 0:
    
    K = lst[(M-1 + i)%len(lst)]
    a = lst.index(K)
    sol.append(K)
    lst.remove(K)
    i = a

print('<', end="")
print(", ".join(map(str, sol)), end="")
print('>', end="")