import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = {}
# lst_site = set()

for i in range(N):
    site, pw = input().split()
    lst[site]= pw

for _ in range(M):
    A = input().split()
    print(lst[A[0]])
