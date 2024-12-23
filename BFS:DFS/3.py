n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


from collections import deque
def bfs(graph, start):
    q = deque([start])
    visited = []
    
    while q:
        node = q.popleft()
        
        if node not in visited:
            visited.append(node)
        
        for n in graph[node]:
            if n not in visited:
                q.append(n)
                
    return len(visited)

print(bfs(graph, 1)-1)




def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)
    
    return len(visited)
# print(bfs(graph, 1)-1)
