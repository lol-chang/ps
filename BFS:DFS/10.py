from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def next():
    melt = [[0] * m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                side = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        side += 1
                melt[x][y] = side

    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                graph[x][y] -= melt[x][y]
                if graph[x][y] < 0:
                    graph[x][y] = 0

def bfs():
    visited = [[False] * m for _ in range(n)]
    count = 0

    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0 and not visited[x][y]:
                queue = deque([(x, y)])
                visited[x][y] = True
                while queue:
                    cx, cy = queue.popleft()
                    for i in range(4):
                        nx, ny = cx + dx[i], cy + dy[i]
                        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                count += 1
    return count

year = 0

while True:
    iceberg_count = bfs()

    if iceberg_count >= 2:
        print(year)
        break

    if iceberg_count == 0:
        print(0)
        break

    next()
    year += 1
