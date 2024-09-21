import sys

input = sys.stdin.readline

N = int(input())
lst = []
cnt = 1
num_lst = []
chk = []
asw = []

for i in range(1, N+1):
    
    num = int(input())
    num_lst.append(num)

    while cnt <= num:
        lst.append(cnt)
        asw.append('+')
        # print(lst)
        cnt += 1

    if lst[-1] == num:
        a = lst.pop()
        asw.append('-')
        chk.append(a)

if num_lst != chk:
    print('NO')
else:
    for i in asw:
        print(i)
    
