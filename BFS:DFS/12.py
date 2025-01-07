n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#     북  동  남  서 
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


# ------------------------ Another Version -------------
from collections import deque
def using_queue(n, m, x, y, d, graph):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y, d)])  # 큐에 현재 위치와 방향 저장
    cleaned_count = 0

    while queue:
        x, y, d = queue.popleft()

        # 1. 현재 위치를 청소
        if not visited[x][y]:
            visited[x][y] = True
            cleaned_count += 1

        # 2. 4방향 탐색
        cleaned = False
        for _ in range(4):
            d = (d - 1) % 4  # 왼쪽 방향으로 회전
            nx, ny = x + dx[d], y + dy[d]

            # 청소 가능한 공간인지 확인
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                queue.append((nx, ny, d))  # 다음 위치와 방향 저장
                cleaned = True
                break

        # 3. 4방향 모두 청소되어 있거나 벽인 경우 후진
        if not cleaned:
            nx, ny = x - dx[d], y - dy[d]  # 후진
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny, d))  # 방향 유지하며 후진
            else:
                break  # 후진 불가능하면 종료

    return cleaned_count
#print(using_queue(n, m, x, y, d, graph))
