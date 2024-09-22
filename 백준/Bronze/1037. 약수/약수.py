import sys

input = sys.stdin.readline

N = int(input())

M = list(map(int, input().split()))

M.sort()

print(M[-1]*M[0])