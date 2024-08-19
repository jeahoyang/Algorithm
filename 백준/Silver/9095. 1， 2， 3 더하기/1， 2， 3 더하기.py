import sys

input = sys.stdin.readline

T = int(input())

dp = [0]*(11)
dp[1] = 1
dp[2] = 2
dp[3] = 4


for _ in range(T):
    A = int(input())


    for i in range(1, A+1):

        if i > 3:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


    print(dp[A])