n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

from collections import deque

# 이것 따로 구현해봄.
# 방문한 곳 재방문 방지 
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))


    while q:
        x,y = q.popleft()
        visited[x][y]=True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                                    # +) 
            if graph[nx][ny]==0 or visited[nx][ny]:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1 
                q.append((nx,ny))
    
    return graph[n-1][m-1]

print(bfs(0,0))

for i in graph:
    print(i)