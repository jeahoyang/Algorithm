import sys

N = int(input())

lst = list(map(int, input().split()))
lst.sort()

print(sum(lst)/lst[-1]*100/N)