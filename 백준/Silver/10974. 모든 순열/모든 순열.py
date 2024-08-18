import sys

input = sys.stdin.readline

N = int(input())
lst = []

for i in range(1, N+1):
    lst.append(i)

print(" ".join(map(str, lst)))

# lst = list(map(int, input().split()))

lst_sort = sorted(list(lst), reverse=True)
# print(lst_sort)

while lst != lst_sort:
    for j in range(N-1, 0, -1):

        if lst[j] > lst[j-1]:
            # print(lst)
            A = sorted(list(lst[j:]))
            # print(A)
            # print(len(A))

            for k in range(len(A)):
                # print(A[k], lst[j-1])
                if lst[j-1] < A[k]:
                    lst[j-1] , A[k] = A[k], lst[j-1]
                    # print("succes")
                
                    break

            print(" ".join(map(str, lst[:j]+A)))
            lst = lst[:j]+A
            break

# print(" ".join(map(str, lst[:j]+A)))




