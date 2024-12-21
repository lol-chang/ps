n, m, v = map(int, input().split())
gragh = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    gragh[x].append(y)
    gragh[y].append(x)

for g in gragh:
    g.sort()


from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = []

    while q:
        node = q.popleft()

        if node not in visited:
            visited.append(node)

        for i in gragh[node]:
            if i not in visited:
                q.append(i)

    return visited

def dfs(graph, start, visited = None):
    if visited is None:
        visited = []
    
    visited.append(start)
    
    for i in gragh[start]:
        if i not in visited:
            dfs(graph, i, visited)

    return visited


for i in dfs(gragh, v):
    print(i, end=' ')

print()

for i in bfs(gragh, v):
    print(i, end=' ')