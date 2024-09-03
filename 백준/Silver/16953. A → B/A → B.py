import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0

def sol(N, M, cnt):
    while M%2 != 1 and M > N:
        cnt += 1
        M = M//2
        # print(M)





    if M > N and int(str(M)[-1]) == 1:
        if M%2 == 1:
            M = int(str(M)[:-1])
            # print(M)
        cnt += 1
        # print(M)
        # print(cnt)
        sol(N, M, cnt)
    elif M == N:
        # print('aaaaaaaa')
        print(cnt+1)
        return 
    else:
        print(-1)
        return
    

sol(N, M, cnt)


