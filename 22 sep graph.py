"""
1 задание
"""

# n = int(input())
#
# parent = [0] * n
#
# for i in range(n):
#     p = int(input())
#     parent[i] = p - 1 if p != -1 else -1
#
# print(parent)
#
# def depth(employee):
#     d = 1
#
#     while parent[employee] != -1:
#         employee = parent[employee]
#         d += 1
#
#     return d
#
# answer = 0
#
# for i in range(n):
#     answer = max(answer, depth(i))
#     print(depth(i))
#
# print(answer)


"""
2 задание
"""
#
# n = int(input())
# f = list(map(int, input().split()))
#
# for i in range(n):
#     a = i
#     b = f[a] - 1
#     c = f[b] - 1
#
#     if f[c] - 1 == a:
#         print("YES")
#         break
# else:
#     print("NO")


"""
3 задание
"""

# n, m = map(int, input().split())
#
# cats = list(map(int, input().split()))
#
# graph = [[] for _ in range(n)]
#
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#
#     graph[a].append(b)
#     graph[b].append(a)
#
# print(graph)
# answer = 0
#
#
# def dfs(node, parent, cats_in_row):
#     global answer
#
#     if cats[node] == 1:
#         cats_in_row += 1
#     else:
#         cats_in_row = 0
#
#     if cats_in_row > m:
#         return
#
#     children = 0
#
#     for next_node in graph[node]:
#         if next_node == parent:
#             continue
#
#         children += 1
#         dfs(next_node, node, cats_in_row)
#
#     if children == 0:
#         answer += 1
#
#
# dfs(0, -1, 0)
#
# print(answer)


"""
4 задание
"""

from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    color = [-1] * n
    color[0] = 0

    q = deque([0])

    while q:
        v = q.popleft()

        for u in g[v]:
            if color[u] == -1:
                color[u] = 1 - color[v]
                q.append(u)

    a = [i + 1 for i in range(n) if color[i] == 0]
    b = [i + 1 for i in range(n) if color[i] == 1]

    ans = a if len(a) <= len(b) else b

    print(len(ans))
    print(*ans)