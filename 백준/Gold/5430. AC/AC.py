import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def R():
    dq.reverse()

    return dq

def D():
    dq.popleft()

    return dq

for _ in range(T):
    p = list(map(str, input().split()))
    n = int(input())
    lst = input()
    dq = deque()
    chk = 0
    er = 0

    
    import re

    # print(dq)
    numbers = re.findall(r'\d+', lst)

    # 추출한 숫자들을 정수로 변환하여 deque에 저장
    dq = deque(int(x) for x in numbers)
    # output = ','.join(str(x) for x in dq)
    # dq([output])

    # dq = deque(int(x) for x in lst if x.isdigit())
    # print(dq)
    # print(numbers,"number")

    # print(p[0])
    for i in p[0]:
        if i == 'R':
            if len(dq) == 0:
                # print('error')
                pass
            else:
                pass
            chk += 1
        elif i == 'D':
            # print(dq, len(dq))
            if len(dq) == 0:
                print('error')
                er = 1
                break
            else:
                if chk % 2 == 0:
                    D()
                else:
                    dq.pop()

    # print(er, dq)
    if len([int(x) for x in dq]) == 0:
        if er == 0:
            print([])
            # if p[0][-1] == 'R':
            #     print([])
            # else:
            #     pass
        else:
            pass
    else:
        if chk % 2 == 1:
            R()
        else:
            pass

        output = ','.join(str(x) for x in dq)
        # if len(output) == 0:
        #     pass
        # else:
        print('[',end ="")
        print(output, end="")
        print(']')
        # print([",".join(map(str, dq))])


