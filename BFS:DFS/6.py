from collections import deque

def bfs(tomatoes):
    q = deque(tomatoes)

    dk = [-1, 1, 0, 0, 0, 0]
    dx = [ 0, 0, -1, 1, 0, 0]
    dy = [ 0, 0, 0, 0, -1, 1]

    while q:
        k, x, y = q.popleft()

        for i in range(6):
            nk = k + dk[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if nk < 0 or nx < 0 or ny < 0 or nk >= h or nx >= m or ny >= n:
                continue

            if graph[nk][nx][ny] == -1:
                continue

            if graph[nk][nx][ny] == 0:
                graph[nk][nx][ny] = graph[k][x][y] + 1
                q.append((nk, nx, ny))

    max_days = 0
    for k in range(h):
        for x in range(m):
            for y in range(n):
                if graph[k][x][y] == 0:  
                    return -1
                max_days = max(max_days, graph[k][x][y])

    return max_days - 1

n, m, h = map(int, input().split())

graph = []

for k in range(h):
    graph.append([])
    for x in range(m):
        graph[k].append(list(map(int, input().split())))

tomatoes = [(k, x, y) for k in range(h) for x in range(m) for y in range(n) if graph[k][x][y] == 1]

result = bfs(tomatoes)
print(result)
