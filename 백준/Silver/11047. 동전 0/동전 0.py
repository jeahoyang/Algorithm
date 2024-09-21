import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
lst_i = []

for i in range(N):
    coin = int(input())
    lst.append(coin)
    if coin <= K:
        lst_i.append(i)

cnt = 0

lst.append(100000001)

if K%lst[lst_i[-1]] == 0:
    print(K//lst[lst_i[-1]])
else:
    while K%lst[lst_i[-1]+1] != 0:
        

        cnt += K//lst[lst_i[-1]]
        # print(cnt)

        K = K%lst[lst_i[-1]]
        lst_i[-1] -= 1
        # print(K)


    if K < 5:
        print(cnt + K)
    else:
        print(cnt)