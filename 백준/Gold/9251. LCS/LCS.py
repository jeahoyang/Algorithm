import sys

input = sys.stdin.readline

lst1 = str(input().strip())
lst2 = str(input().strip())

LCS = [[0]*(len(lst2)+1) for _ in range(len(lst1)+1)]

for i in range(1, len(lst1)+1):
    for j in range(1, len(lst2)+1):
        if lst1[i-1] == lst2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

print(LCS[-1][-1])