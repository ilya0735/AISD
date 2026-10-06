"""
1 задание
"""

# n = int(input())
#
# passwords = set()
#
# for num in range(n):
#     password = input()
#     if password not in passwords:
#         passwords.add(password)
#         print('OK')
#     else:
#         print(password)



"""
2 задание
"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = {}
    ans = 0

    for i in range(n):
        x = a[i] - (i + 1)
        if x in cnt:
            ans += cnt[x]

        cnt[x] = cnt.get(x, 0) + 1

    print(ans)