import sys
input = sys.stdin.readline

N = int(input())
per = list(map(int, input().split()))
B = 0

if N == 1:
    print(-1)
else:
    for i in range(N-1, 0, -1):
        if per[i] < per[i-1]:
            B = sorted(list(per[i:]), reverse=True)
            for j in range(N-i):
                if B[j] < per[i-1]:
                    B[j], per[i-1] = per[i-1], B[j]
                    # print(j, B[j], per[i-1])
            # A = sorted(list(per[i:]), reverse=True)
                    break

                
            break


    if B == 0:
        print(-1)
    else:

        result = " ".join(map(str, list(per[:i]) + B))


        print(result)


    