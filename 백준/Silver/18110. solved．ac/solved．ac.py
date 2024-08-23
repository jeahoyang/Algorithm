import sys

input = sys.stdin.readline

N = int(input())

def rounding(num):
    if num%2 == 0.5:
        return round(num)+1
    else:
        return round(num)


a = rounding(N*0.15)
lst = []
lst2 = []


for i in range(N):
    lev = int(input())
    lst.append(lev)

if N == 0:
    print(0)
    # lst2.append(0)
else:
    lst.sort()
    lst2 = list(lst[a:(N-a)])
    print(rounding(sum(lst2)/len(lst2)))