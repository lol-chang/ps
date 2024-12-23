n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

from collections import deque

def bfs(graph, start, end):
    q = deque([start])
    visited = set()
    
    res = 0
    while q:
        # 방문 노드 개수가 아니라, 레벨 단위 처리가 핵심
        for _ in range(len(q)):
            node = q.popleft()
            visited.add(node)
        
            if end == node:
                return res
        
            for n in graph[node]:
                if n not in visited:
                    q.append(n)
        res+=1
    return -1
    
print(bfs(graph, s, e))
