import sys

input = sys.stdin.readline

L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
# start = 1
# print(lst[start:])
vowel = ['a', 'e', 'i', 'o', 'u']

password = []

def count(password):
    v_count = 0
    for i in password:
        if i in vowel:
            v_count += 1
    return v_count


start = 0
def sol(start):

    if count(password) > 0 and len(password) - count(password) > 1:
        if len(password) == L:
            print("".join(map(str, password)))
            # print(password)
            return



    for i in lst[start:]:
        if password[-1] < i:
            password.append(i)
            sol(start+1)
            password.pop()
        # print(password)

for i in lst:
    password.append(i)
    sol(0)
    password.pop()
