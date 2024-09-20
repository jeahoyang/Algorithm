import sys
import copy

input = sys.stdin.readline

N = int(input())
lst = []

prev_max = [0] * 3
prev_min = [0] * 3
cur_max = [0] * 3
cur_min = [0] * 3


for i in range(N):
    lst = list(map(int, input().split()))
    # print(lst)

    # print(prev_max)
    cur_max[0] = lst[0] + max(prev_max[0], prev_max[1])
    cur_max[1] = lst[1] + max(prev_max[0], prev_max[1], prev_max[2])
    cur_max[2] = lst[2] + max(prev_max[1], prev_max[2])
    # print(prev_max[1])
    # print(lst[1], max(prev_max[0], prev_max[1], prev_max[2]))


    cur_min[0] = lst[0] + min(prev_min[0], prev_min[1])
    cur_min[1] = lst[1] + min(prev_min[0], prev_min[1], prev_min[2])
    cur_min[2] = lst[2] + min(prev_min[1], prev_min[2])

    # print(prev_max, "before")
    prev_max = cur_max[:]
    # print(prev_max, " after")
    prev_min = cur_min[:]

print(max(prev_max), min(prev_min))
        

