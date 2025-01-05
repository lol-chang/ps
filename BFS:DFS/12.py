n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]
count = 0

while True:
    if not visited[x][y]:
        visited[x][y] = True
        count += 1

    
    cleaned = False
    for _ in range(4):
        d = (d - 1) % 4  
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
            x, y = nx, ny
            cleaned = True
            break

    
    if not cleaned:
        nx, ny = x - dx[d], y - dy[d]  
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break  

print(count)
