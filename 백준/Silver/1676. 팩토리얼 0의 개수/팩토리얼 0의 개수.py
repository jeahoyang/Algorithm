import sys
input = sys.stdin.readline
N = int(input())

A = N // 5 
if N >= 25 :
    if N >= 125:
        print(A+A//5+A//5//5)
        pass
    else:
        print(A+A//5)
else:
    print(A)