import sys

input = sys.stdin.readline

N, K  = map(int, input().split())
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))


dp = [0 for _ in range(K+1)]

for i in lst:
    w = i[0]
    v = i[1]

    for j in range(K,w-1,-1):
        
        dp[j] = max(dp[j], dp[j-w] + v)
        # print(K-j, dp[j])

print(max(dp))