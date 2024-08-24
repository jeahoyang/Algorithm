import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst_N = set()
lst_M = set()
sol = set()

for i in range(N):
    A = input()
    # print(A)
    lst_N.add(A[:-1])



for i in range(M):
    B = input()
    lst_M.add(B[:-1])

# # print(lst_M)
# for i in lst_M:
#     # print(i)
#     if i in lst_N:
#         sol.add(i)
#         lst_N.remove(i)
#         continue


sorted_set = sorted(list(lst_N & lst_M))
print(len(sorted_set))
# print(sorted_set)


for item in sorted_set:
    print(item)