import sys

input = sys.stdin.readline

N = int(input())
age = []
name = []
# A = {}
lst= []

for _ in range(N):
    age, name = map(str, input().split())
    # A[name] = age
    lst.append([int(age), name])

K = sorted(lst, key=lambda x:x[0])

for i in range(N):
    print(" ".join(map(str, K[i])))